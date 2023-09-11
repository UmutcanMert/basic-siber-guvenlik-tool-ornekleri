from scapy.all import *

# send continuous request packets.

conf.checkIPaddr = False


ether = Ether(dst='ff:ff:ff:ff:ff:ff')

ip = IP(src="0.0.0.0", dst ='255.255.255.255')

udp = UDP(sport=68, dport=67)

# scapy-> ls(BOOTP)
bootp = BOOTP(op=1, chaddr=RandMAC())

# scapy-> ls(DHCP)
dhcp = DHCP(options=[("message-type","discover"),"end"])

# create a package
dhcp_discover = ether/ip
dhcp_discover = dhcp_discover/udp
dhcp_discover = dhcp_discover/bootp
dhcp_discover = dhcp_discover/dhcp

for i in range(10):
	answer, unanswer = srp(dhcp_discover, iface='eth0', verbose=False) 
	for p in answer:
		print(p[1].dst,":",p[1].yiaddr)
	#sendp(dhcp_discover, iface='eth0', verbose=False, loop=1)