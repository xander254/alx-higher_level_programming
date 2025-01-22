#!/bin/bash
# Script to display the status code of a URL response
curl -s -o /dev/null -w "%{http_code}" "$1"
