import sys
from nmap3 import Nmap


ip = sys.argv[1]

def port_scanner(ip):
    nmap = Nmap()
    results = nmap.scan_top_ports(ip)

    for port in results[ip]['ports']:
        port_num = port['portid']
        port_state = port['state']
        print(f"Port {port_num} is {port_state}")

port_scanner(ip)

