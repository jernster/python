import argparse
import ipaddress

parser = argparse.ArgumentParser(description="IPV4 Subnet Generator")
parser.add_argument("--cidr", help="CIDR in the form of 192.168.1.0/24", required=True) 

args = parser.parse_args()

cidr = args.cidr

net = ipaddress.ip_network(cidr)

print("{0} addresses in {1}".format(net.num_addresses, cidr))
print(end='\n')

for a in net:
    print(a)