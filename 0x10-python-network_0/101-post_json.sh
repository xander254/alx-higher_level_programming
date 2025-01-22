#!/bin/bash
# A bash script to send a json file to the server using url
jq empty "$2" >/dev/null 2>&1 || { echo "Not a valid JSON"; exit 1; } curl -X POST -d @"$2" -H "Content-Type: application/json" "$1" echo ""
