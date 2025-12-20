#!/usr/bin/env python
import scapy.all as scapy
import optparse

parser = optparse.OptionParser()
parser.add_option("-t","--target",dest = "target",help="Enter the Target IP")
(option,arg) = parser.parse_args()
target = option.target

def ARP_Scan(ip):
    # Using ARP to ask who has target IP
    arp_request = scapy.ARP(pdst=ip)
    # Broadcast MAC ADDRESS
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    # Sending the ARP_BroadCast
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    client_list = list()
    for element in answered:
        client_dic = dict()
        client_dic["IP_Address"] = element[1].psrc
        client_dic["MAC_Address"] = element[1].hwsrc
        client_list.append(client_dic)
    return client_list

def print_res(answered):
    print("IP ADDRESS\t\t\tMAC ADDRESS\n---------------------------------------")
    for element in answered:
        print(element["IP_Address"] + "\t\t" + element["MAC_Address"])
client = ARP_Scan(target)
print_res(client)