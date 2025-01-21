#!/bin/bash
# Display the body of a 200 status code response
[ "$(curl -s -o /dev/null -w "%{http_code}" -L "$1")" = "200" ] && curl -sL "$1"
