from logs import logDecorator as lD
import json, psycopg2

from lib.celery.App import app


config = json.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + 'lib.worker.worker_1'

@app.task
@lD.log(logBase + '.add')
def add(logger, a, b):

    try:
        result = a+b
        return result
    except Exception as e:
        logger.error('Unable to log the task: {e}')
        return None

    return 
