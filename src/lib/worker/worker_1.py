from logs import logDecorator as lD
import json, psycopg2

from lib.celery.App import app

config = json.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + 'lib.worker.worker_1'

@app.task
@lD.log(logBase + '.add')
def add(logger, a, b):
    '''add two supplied items
    
    This example takes two arguments and adds them together. This
    is much like the function available with 
    
    Parameters
    ----------
    logger : {[type]}
        [description]
    a : {[type]}
        [description]
    b : {[type]}
        [description]
    
    Returns
    -------
    [type]
        [description]
    '''

    try:
        result = a+b
        return result
    except Exception as e:
        logger.error('Unable to log the task: {e}')
        return None

    return 
