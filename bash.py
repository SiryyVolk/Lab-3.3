#!/bin/bash
subnet="192.168.1"
for i in {1..254}; do
  ip="$subnet.$i"
  (ping -c1 -W1 $ip &>/dev/null && echo "[+] $ip alive") &
done
wait