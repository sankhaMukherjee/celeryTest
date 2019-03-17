import json, argparse

from importlib      import util
from logs           import logDecorator  as lD
from lib.testLib    import simpleLib     as sL
from lib.argParsers import addAllParsers as aP

import numpy as np

config   = json.load(open('../config/config.json'))
logBase  = config['logging']['logBase']
logLevel = config['logging']['level']
logSpecs = config['logging']['specs']

@lD.log(logBase + '.importModules')
def importModules(logger, resultsDict):
    '''import and execute required modules
    
    This function is used for importing all the 
    modules as defined in the ../config/modules.json
    file and executing the main function within it
    if present. In error, it fails gracefully ...
    
    Parameters
    ----------
    logger : {logging.Logger}
        logger module for logging information
    '''
    modules = json.load(open('../config/modules.json'))

    for m in modules:

        try:
            if not m['execute']:
                logger.info('Module {} is being skipped'.format(m['moduleName']))
                continue
        except Exception as e:
            logger.error('Unable to check whether ')

        try:
            name, path = m['moduleName'], m['path']
            logger.info('Module {} is being executed'.format( name ))

            module_spec = util.spec_from_file_location(
                name, path)
            module = util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)
            module.main(resultsDict)
        except Exception as e:
            print('Unable to load module: {}->{}\n{}'.format(name, path, str(e)))

    return

def main(logger, resultsDict):
    '''main program
    
    This is the place where the entire program is going
    to be generated.
    '''

    # First import all the modules, and run 
    # them
    # ------------------------------------
    importModules(resultsDict)

    from lib.worker import worker_1

    result = worker_1.add.delay(2, 2)
    for i in range(100):
        print(result.state)

    if result.state == 'SUCCESS':
        r = result.get()
        print(f'The result of this calculation is: {r}')

    
    results = [worker_1.add.delay(*np.random.randn( 2 )) for i in range(10000)]
    while True:
        done    = [ r.state == 'SUCCESS' for r in results]
        tempResults = [ r.get() for r in results if r.state == 'SUCCESS']
        print( 'Percentage done:{}, mean --> {}'.format(sum(done)*100.0/len(done), np.mean(tempResults) ))
        if all(done):
            done = [ r.get() for r in results ]
            break

    return

if __name__ == '__main__':

    # Let us add an argument parser here
    parser = argparse.ArgumentParser(description='celeryTest command line arguments')
    parser = aP.parsersAdd(parser)
    results = parser.parse_args()
    resultsDict = aP.decodeParsers(results)

    # ---------------------------------------------------
    # We need to explicitely define the logging here
    # rather than as a decorator, bacause we have
    # fundamentally changed the way in which logging 
    # is done here
    # ---------------------------------------------------
    logSpecs = aP.updateArgs(logSpecs, resultsDict['config']['logging']['specs'])
    try:
        logLevel = resultsDict['config']['logging']['level']
    except Exception as e:
        print('Logging level taking from the config file: {}'.format(logLevel))

    logInit  = lD.logInit(logBase, logLevel, logSpecs)
    main     = logInit(main)

    main(resultsDict)