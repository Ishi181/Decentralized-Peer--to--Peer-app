from chat_client.chat_node import listen_for_messages, send_message
from encryption.crypto_utils import generate_keys, serialize_public_key, deserialize_public_key
import threading

def main():
    # Generate own keys
    private_key, public_key = generate_keys()

    # Show your public key for manual sharing
    print("=== Your public key ===")
    print(serialize_public_key(public_key))
    print("=======================")

    # Input peer info
    my_port = int(input("Enter your listening port: "))
    peer_ip = input("Enter peer IP (default: 127.0.0.1): ") or "127.0.0.1"

    # Ask user to paste peer's public key PEM
    print("\nPaste your peer's public key PEM (including the -----BEGIN PUBLIC KEY----- lines):")
    peer_pub_pem = ""
    while True:
        line = input()
        peer_pub_pem += line + "\n"
        if "END PUBLIC KEY" in line:
            break

    peer_public_key = deserialize_public_key(peer_pub_pem)

    peer_port = int(input("Enter peer's listening port: "))

    # Start listener thread
    listener_thread = threading.Thread(target=listen_for_messages, args=(my_port, private_key))
    listener_thread.daemon = True
    listener_thread.start()

    # Sending loop
    while True:
        msg = input("Enter message (or 'exit' to quit): ")
        if msg.lower() == 'exit':
            break
        send_message(peer_ip, peer_port, msg, peer_public_key)

if __name__ == "__main__":
    main()
