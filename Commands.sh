#!/bin/bash
# command ./inurlbr.php -s scan-list20180314.lst \
# 	--dork-file='/root/stuff/source/inurlbr-results/Dorks/RFI/RFI-dorks-mini.lst' \
# 	--tor-random --exploit-get "?'0x27%27" \
# 	--exploit-vul-id 1,2,13,14,4,9 	\
# 	-q 1,2,3,4,5,6 --mp 3 -T 1 		\
# 	--custom-config K00B404.conf 	\
# 	--blacklist .zabanuch.profitux.cz.,.vulnweb.,.teamgear.


DBPATH="/root/stuff/tools/PWR_inurl/output/PWR_inurl_DB.sqlite3"
FOLDER="/root/stuff/tools/PWR_inurl/output/$1/nmap_output.lst"
for i in $(cat $FOLDER |grep 'open port'|sort -u);do  
	Ports=$(echo $i|awk -F '/' '{print $1}'|tr -d 'httpproxysynackeubmii-lDvd')
	if [[ ! -z "${Ports##*[!0-9]*}" ]] ;then  
		PortsString+=$(echo $Ports | tr -s "\n" ":")
	fi	
done
PortsString=`echo $PortsString |sed 's/:$//'`
R=$(sqlite3 $DBPATH "SELECT ports FROM BigDump where www like '%$1%'")
if [[  $R != $PortsString ]]; then
	$(sqlite3 $DBPATH "UPDATE BigDump set ports = '$PortsString' where www like '%$1%' limit 1;")
	echo "Written "$R"!"
fi

function StringVervang(){
	needle=$1
	replacement=$2
	hay=$3
	${hay//$replacement/$needle}
}
function GeoSet(){
	R=$(sqlite3 $DBPATH "SELECT raw_loot FROM BigDump where www like '%$1%'")
	if [[ $R ]]; then
		echo $R |grep 'DBA:'
	fi
}
GeoSet $1