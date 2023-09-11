from scapy.all import *
from scapy.layers.inet import ICMP, IP
import threading

address = "10.0.2."

ip_list = []
lock = threading.Lock()

# with using thread, this code more run execute


def ping_target(ip_address):
    ip = IP(dst=ip_address)
    icmp = ICMP()
    ping_packet = ip / icmp

    response = sr1(ping_packet, timeout=0.5, verbose=False)
    if response:
        with lock:
            ip_list.append(ip_address)


# Create a list to hold thread objects
threads = []

# Launch threads to send ping packets to different IP addresses
for i in range(100):
    target_ip = address + str(i)
    thread = threading.Thread(target=ping_target, args=(target_ip,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("OPEN IP:")
print(ip_list)
