from scapy.all import *
from scapy.layers.inet import ICMP, IP
from scapy.layers.l2 import Ether, ARP

eth = Ether()
arp = ARP()

eth.dst = "ff:ff:ff:ff:ff:ff"

arp.pdst = "10.0.2.1/24"

# eth/arp ifadesi, Scapy'nin ağ paketi oluşturma yeteneklerini kullanarak
# Ethernet (katman 2) ve ARP (Address Resolution Protocol) (katman 3)
# başlıklarını birleştiriyor. Bu tür işlemler Scapy ile ağ paketleri
# oluşturmanın yaygın bir yolu olarak kullanılır.
bc_packet = eth / arp

answer, un_answer = srp(bc_packet, timeout=5)

#answer.summary()
#print("#"*30)
#un_answer.summary()

for snd, rcv in answer:
    print(rcv.psrc," : ",rcv.src)
