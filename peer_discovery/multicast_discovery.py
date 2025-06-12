# peer_discovery/multicast_discovery.py
import socket

MULTICAST_GROUP = '224.1.1.1'
PORT = 5007

def announce_peer(name):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ttl = 1
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    message = f'PEER:{name}'.encode()
    sock.sendto(message, (MULTICAST_GROUP, PORT))
