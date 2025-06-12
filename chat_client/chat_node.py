import socket
import threading
from encryption.crypto_utils import encrypt_message, decrypt_message

def listen_for_messages(port, private_key):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
    sock.listen(5)
    print(f"[LISTENING] on port {port}...")
    while True:
        conn, addr = sock.accept()
        data = conn.recv(4096)
        try:
            message = decrypt_message(private_key, data)
            print(f"[RECEIVED from {addr}] {message}")
        except Exception as e:
            print(f"[ERROR] Failed to decrypt message from {addr}: {e}")
        conn.close()

def send_message(ip, port, message, peer_public_key):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    encrypted_msg = encrypt_message(peer_public_key, message)
    sock.send(encrypted_msg)
    sock.close()
