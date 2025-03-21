#!/bin/bash

clear
echo 

echo "######################"
echo "# System Uptime Info #"
echo "######################"

uptime

echo

echo "######################"
echo "#   CPU Stats Info   #"
echo "######################"

top -bn1 | grep "%Cpu(s):" | cut -d ',' -f 4 | awk '{print "Usage: " 100-$1 "%"}'

echo

echo "######################"
echo "#   RAM Stats Info   #"
echo "######################"

top -bn1 | grep "MiB Mem :" | awk -F '[, ]+' '{print "Free Mem: " $6 " - " int(($6*100)/$4) "%" "\nUsed Mem: " $8 " - " int(($8*100)/$4) "%"}'

echo

echo "######################"
echo "#   Disk Stats Info  #"
echo "######################"

df -h --total | grep "total" | awk '{print "Used Disk: " $3 " - " $5 "\nFree Disk: " $4 " - " 100-$5 "%"}'

echo

echo "##########################"
echo "# Top 5 Processes by CPU #"
echo "##########################"

top -bn1 -o %CPU | head -n 12 | tail -n 6

echo

echo "##########################"
echo "# Top 5 Processes by RAM #"
echo "##########################"

top -bn1 -o %MEM | head -n 12 | tail -n 6