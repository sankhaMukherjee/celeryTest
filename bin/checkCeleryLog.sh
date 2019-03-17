#!/bin/bash 

logFile=$(ls logs/celery_*.log | sort | tail -n1)

cat $logFile
