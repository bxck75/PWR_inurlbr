#!/bin/bash
DBPATH="/root/stuff/tools/PWR_inurl/output/PWR_inurl_DB.sqlite3"
FOLDER="/root/stuff/tools/PWR_inurl/output/"
while read line; do
echo $line >> resultloothandler.tmp
done < <(sqlite3 -separator $',' $DBPATH "SELECT ip,ports FROM BigDump where ports != ''") 


for p in $(cat resultloothandler.tmp); do
	ip=`echo "$p" |awk -F, '{print $1}'`
	port=`echo "$p" |awk -F, '{print $2}'`
	#echo $ip":"$port
	#echo $port
	OLDIFS=$IFS
	IFS=:
	while read p
	do
		echo $p
	done < $port
	IFS=$OLDIFS
	exit
	for i in $(echo $port|awk -F':' '{print }'); do
		echo ${ip}":"${i} >> outfile.tmp
	done
done
cat outfile.tmp |sort -u
rm resultloothandler.tmp