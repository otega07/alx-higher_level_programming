#!/bin/bash
# This Bash script sends a GET request to a URL and prints the size of the response body
curl -s "$1" | grep -i Content-Length | awk '{print $2}'
