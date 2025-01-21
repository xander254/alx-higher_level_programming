#!/bin/bash
# Display the body of a 200 status code response
curl -sL -w "%{http_code}" "$1" | awk '/200$/{exit}1'
