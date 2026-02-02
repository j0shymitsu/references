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
    print(f"Scanning {target}")
    scanner.scan(target, arguments='-F')
    # args = 100 most common ports (rate limiting issues)

    open_ports = scanner[target].get('tcp', {})
    if open_ports:
        for port, info in open_ports.items():
            print(f"Port {port}: {info['name']} is open")
    else:
        print(f"No open ports on {target}")

    print("\n\n")
