#!/usr/bin/env python
from scapy.all import sr1, IP, ICMP

##conf.verb=0

address= "8.8.8.8"

hops = []

for i in range(1, 20):
    res = sr1(IP(dst=address, ttl=i)/ICMP(), timeout=2)
    if res is not None:
        hops.append(res.src)
        if res.src == address:
            break

for addr in hops:
    print(addr)