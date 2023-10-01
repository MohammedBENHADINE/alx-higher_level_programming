#!/bin/bash
# script to output size of bytes sent by http server
curl -s "$1" | wc -c
