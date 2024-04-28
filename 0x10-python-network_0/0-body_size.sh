#!/usr/bin/bash
# cURL get body size
curl -s "$1" | grep -i Content-Length | awk '{print $2}'
