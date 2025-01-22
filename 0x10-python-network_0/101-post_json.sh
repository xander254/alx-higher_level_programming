#!/bin/bash
# A bash script to send a json file to the server using url
jq empty "$2" >/dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "Valid JSON"
else 
    echo "Not a valid JSON"
    exit 1
fi

curl -X POST -d @"$2" -H "Content-Type: application/json" "$1" 
echo ""
