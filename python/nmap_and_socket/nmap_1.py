import nmap

network_range = "192.168.1.0/24"
scanner = nmap.PortScanner()
scanner.scan(hosts=network_range, arguments="-sn")

alive_hosts = []
for host in scanner.all_hosts():
    if scanner[host].state() == "up":
        alive_hosts.append(host)

print(len(alive_hosts), " hosts are alive")
print("Alive hosts: ", alive_hosts)

