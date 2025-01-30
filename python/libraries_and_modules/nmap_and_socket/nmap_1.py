import nmap

scanner = nmap.PortScanner()
scanner.scan(hosts="192.168.0.0/24", arguments="-sn -PR -e eno1")
# args = ping scan; ARP only (LAN); forces correct network interface

alive_hosts = []
for host in scanner.all_hosts():
    if scanner[host].state() == "up":
        alive_hosts.append(host)

print(len(alive_hosts), " hosts are alive")
print("Alive hosts: ", alive_hosts)
print("\n\n")

for target in alive_hosts:
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments='-sS')
    print("Target: ", target)

    try:
        for port in scanner[target]['tcp']:
            service = scanner[target]['tcp'][port]['name']
            print('port {}: {}'.format(port, service), 'is OPEN')
    except KeyError:
        print("No open ports on ", target)
