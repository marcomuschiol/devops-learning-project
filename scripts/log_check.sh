#!/bin/bash

LOGFILE=~/devops/logs/app.log

echo "----- $(date) -----"

# Check: existiert Datei?
if [ ! -f "$LOGFILE" ]; then
    echo "Logfile not found!"
    exit 1
fi

echo "Checking logs..."

# Anzahl Errors zählen
ERROR_COUNT=$(grep -c "Error" "$LOGFILE")

echo "Error count: $ERROR_COUNT"

if [ "$ERROR_COUNT" -gt 0 ]; then
    echo "ERROR detected!"
else
    echo "System OK"
fi
