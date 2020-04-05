#!/usr/bin/python3

import sys

def ipv4_to_isis_net(ipv4_address, area_prefix='49.0001', net_selector='00'):
  octets = ipv4_address.split('.')
  padded_ip = "".join( [octet.rjust(4,'0') for octet in octets] )
  net_part = ".".join( [padded_ip[index:index+4] for index in range(0, 12, 4)] )
  return area_prefix + '.' + net_part + '.' + net_selector

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print( "USAGE: ./ipv4_to_isis_net.py IPv4_ADDRESS" )
  else:
    print(  ipv4_to_isis_net(sys.argv[1])  )     
