#!/bin/bash 

logFile=$(ls logs/20*.log | sort | tail -n1)

cat $logFile
