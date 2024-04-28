#!/bin/bash
# Sends a DELETE request to the URL passed as first argument and displays response
curl -s -X DELETE "${1}"
