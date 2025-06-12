# 🔐 Decentralized Encrypted P2P Chat

A fully decentralized peer-to-peer chat application with end-to-end encryption using RSA and AES. No central server, no third-party monitoring — just direct, secure messaging between users.

---

## 🚀 Features

- 🧵 **Direct P2P connection** (TCP sockets)
- 🔐 **End-to-End Encryption** using RSA (public-key cryptography)
- 🧠 **Manual Public Key Exchange** (for secure trust)
- 🗣️ Real-time message sending and receiving using multithreading
- 💡 Works on **local network** or over internet (port-forwarding required)

---

## 📂 Project Structure

decentralized_chat/
├── main.py
├── chat_client/
│ └── chat_node.py
└── encryption/
└── crypto_utils.py

yaml
Copy
Edit

---

## 🛠️ Requirements

- Python 3.7+
- Install required packages:

```
pip install cryptography
```
---


## 💻 Usage

Step 1: Run the Chat (2 Terminals / 2 Machines)
Open two terminals, and in both, run:

python main.py
Step 2: Follow the Prompts
Each peer will:

Generate and show its public key

Ask for:

Listening port (e.g., 9000 / 9001)

Peer IP (use 127.0.0.1 for local)

Peer port

Paste the peer’s public key (copy the full PEM block)

Once both peers have exchanged public keys, you can chat securely!

🔒 How It Works
Each peer generates a fresh RSA key pair at startup.

Messages are encrypted with the recipient's public key and decrypted using the recipient's private key.

Manual public key exchange ensures authenticity.

Sockets are used to directly send/receive encrypted data.

📸 Screenshot

📦 TODO / Extras
 Add support for WebRTC (browser-based chat)

 Implement group chat with mesh routing

 Store peer keys securely for future sessions

 Message delivery confirmation and offline buffer

🤝 Contributing
Pull requests are welcome! Feel free to fork and improve the project.

---


## 📝 License
This project is open-source under the MIT License.

---


## 👨‍💻 Author
Name - Ishi Singla
Email - ishisingla181@gmail.com
