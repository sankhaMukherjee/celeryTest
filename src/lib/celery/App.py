from logs import logDecorator as lD
import json, psycopg2
from celery import Celery
import logging

from datetime import datetime as dt


config = json.load(open('../config/config.json'))
logBase = config['logging']['logBase']
logLevel = config['logging']['level']
logSpecs = config['logging']['specs']

cConfig = json.load(open('../config/celery.json'))

app = Celery( 
    cConfig['base']['name'], 
    broker  = cConfig['base']['BROKER_URL'],
    backend = cConfig['base']['BACKEND_URL'],
    include = cConfig['base']['include'])

app.conf.update( **cConfig['extra'] )

