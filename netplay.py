from scapy.all import *
import subprocess

def print_packet(pkt):
    print("Sniffed packet: " + pkt['IP'].src + " to " + pkt['IP'].dst)
    pkt.show()


# sniffing packet based on filter
def sniff_packet_filter(interface, filter_statement):
    packets = sniff(iface=interface, filter=filter_statement, prn=print_packet)

