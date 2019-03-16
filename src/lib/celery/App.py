from logs import logDecorator as lD
import json, psycopg2
from celery import Celery

config = json.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + 'lib.celery.App'

cConfig = json.load(open('../config/celery.json'))

app = Celery( 
    cConfig['base']['name'], 
    broker  = cConfig['base']['BROKER_URL'],
    backend = cConfig['base']['BACKEND_URL'],
    include = cConfig['base']['include'])

app.conf.update( **cConfig['extra'] )

