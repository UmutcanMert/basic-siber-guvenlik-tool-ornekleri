from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.l2 import Ether

packet_list = []

packet_number = int(input("packet number: "))

for i in range(packet_number):
    src_mac = RandMAC()
    dst_mac = RandMAC()
    src_ip = RandIP()
    dst_ip = RandIP()

    ether = Ether(src=src_mac, dst=dst_mac)
    ip = IP(src=src_ip, dst=dst_ip)
    packet = ether / ip
    packet_list.append(packet)
    print(src_mac, ":", src_ip, " >> ", dst_mac, ":", dst_ip)

sendp(packet_list, iface="eth0", verbose=False)
