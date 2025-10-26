#!/usr/bin/env python
import subprocess
import optparse
import re

def Get_Args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="Mac_Address", help="New MAC Address")

    (options, args) =  parser.parse_args()
    if not options.interface:
        #Code to handle error
        parser.error("[-]You must specify an interface to change its MAC Address --help for more information.")
    elif not options.Mac_Address:
        # code to handle error
        parser.error("[-]You must specify a MAC Address --help for more information.")
    return(options.interface, options.Mac_Address)

def Change_Mac(interface, new_mac):
    print("[+] Changing the Mac_Address")
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])

def Current_Mac(interface):
    ifconfig_res = subprocess.check_output(["ifconfig", interface])

    res = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_res))
    if res:
        return res.group(0)
    else:
        print("[-] could not read Mac_Address")
        return None


(interface,Mac_Address) = Get_Args()
print("Current Mac_Address: "+str(Current_Mac(interface)))
Change_Mac(interface, Mac_Address)
cur_mac = Current_Mac(interface)

#Checking the mac address
if cur_mac == Mac_Address:
    print("[+] Mac_Address is successfully changed to "+Mac_Address)
else:
    print("[-] Mac_Address is not changed")

