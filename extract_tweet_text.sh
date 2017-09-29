#!/bin/sh

if [ -f $1 ]; then
	awk -F "\"*,\"*" '{print $3}' $1 > tweets_text.csv
	nlines=$(cat tweets_text.csv | wc -l)
	ntweets=$(expr $nlines - 1)
	tail -$ntweets tweets_text.csv > tweets_text.txt
	rm tweets_text.csv
else
	echo "No such tweets csv file"
fi
