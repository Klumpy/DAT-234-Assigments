#! /bin/bash

# Read IP from user
echo "Enter IP to Ping: "
read IP
IFS=. read ip1 ip2 ip3 ip4 <<< "$IP"

echo -e "\nIPs alive: "

# Ping IPs, and only show those alive
fping -a -q -g $ip1.$ip2.$ip3.1 $ip1.$ip2.$ip3.255
