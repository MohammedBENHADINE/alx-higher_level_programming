#!/bin/bash
# get response from server and display data length

if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

url="$1"
res_file=$(mktemp)
curl -s -o "$res_file" "$url"

echo $(cat "$res_file" | wc -c)
rm -f "$res_file"
