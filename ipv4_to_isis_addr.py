#!/usr/bin/python3

import sys

def ipv4_to_isis_addr(ipv4_address, AFI='49', NET_selector='00'):
	isis_net_addr = ipv4_address.split('.')
	for i in range(0, len(isis_net_addr)):
		while len(isis_net_addr[i]) < 3:
			isis_net_addr[i] = '0' + isis_net_addr[i] # prepend '0' until len = 3		
			isis_net_addr = ''.join(isis_net_addr)
			isis_net_addr = AFI + '.' + isis_net_addr[:4] + '.' + isis_net_addr[4:8] + '.' + isis_net_addr[8:] + '.' + NET_selector
			return isis_net_addr

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print( "USAGE: ./ipv4_to_isis_addr.py IPv4_ADDRESS" )
	else:
		print(  ipv4_to_isis_addr(sys.argv[1])  )			
