#!/bin/bash
# Get no of bytes in response
echo $(curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')
