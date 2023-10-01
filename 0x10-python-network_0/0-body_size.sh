#!/bin/bash
curl -s -o tmp "$1"
echo $(cat tmp | wc -c)
