#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
RESET='\033[0m'


grep "Failed" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | 
while read COUNT IP; do
	if [ "$COUNT" -ge 3 ]; then
		echo -e "${GREEN}$IP${RESET} has been ${RED}banned${RESET} for failed login ${GREEN}$COUNT${RESET} times!"
		iptables -A INPUT -s "$IP" -j DROP
		iptables -A INPUT -s "$IP" -J REJECT
	fi
done

iptables-save | sudo tee /etc/iptables/rules.v4

echo ""
echo -e "${GREEN}All IPs are banned succesfully!!!${RESET}"
echo ""
