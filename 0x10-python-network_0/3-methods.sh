#!/bin/bash
# Display all methods that a http server accepts
curl -sI "$1" | grep -i "Allow" | cut -d " " -f2-
