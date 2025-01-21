#!/usr/bin/env bash
# Get no of bytes in response
URL="$1"
SIZE=$(curl -sI "$URL" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')
if [ -n "$SIZE" ]; then
    echo "$(SIZE)"
fi
