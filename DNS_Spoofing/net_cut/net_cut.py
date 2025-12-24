#!/usr/bin/env/python
import netfilterqueue

def process_packet(packet):
    print(packet)
    packet.drop()
queue = netfilterqueue.NetfilterQueue() #instance of netfilterqueue
queue.bind(0,process_packet) # the queue to get bind with the system queue
queue.run()# to run the queue
