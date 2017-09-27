#!/bin/sh

if [ -f $1 ]; then
	awk -F "\"*,\"*" '{print $3}' $1 > tweets_text.csv
else
	echo "No such tweets csv file"
fi
