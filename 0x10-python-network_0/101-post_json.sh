#!/bin/bash
# A bash script to send a json file to the server using url
curl -X POST -d @"$2" -H "Content-Type: application/json" "$1" 
