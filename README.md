# 🛠️ ARP Spoofing Tool

A lightweight and efficient Python-based ARP spoofing utility using Scapy, designed for network security testing and educational purposes.

> ⚠️ **Disclaimer:** This tool is intended for authorized penetration testing and ethical hacking only. Always obtain explicit permission before performing any kind of network testing.

## ✨ Features

- **Bidirectional ARP Spoofing**: Simultaneously spoofs both the target and gateway to position the attacker as a man-in-the-middle.
- **Automatic MAC Resolution**: Resolves MAC addresses dynamically using ARP requests.
- **Graceful Restoration**: Automatically restores the original ARP tables on interruption (e.g., `CTRL+C`) to prevent network disruption.
- **Command-Line Interface**: Easy-to-use CLI with clear argument parsing via `argparse`.
- **Lightweight & Fast**: Sends spoofed packets in real-time with minimal overhead.

## 🧰 Requirements

- Python 3.x
- [Scapy](https://scapy.net/)
- Root/Administrator privileges (required for sending raw packets)

Install dependencies:
```bash
pip install scapy
```
## 📦 Usage
```bash
sudo python3 arp_spoof.py -t <TARGET_IP> -s <GATEWAY_IP>
```
## Example:
```bash
sudo python3 arp_spoof.py -t 192.168.1.10 -s 192.168.1.1
```
| Option | Description |
| --- | --- |
| -t, --target | Target device IP address |
| -s, --spoof | Gateway or spoofed IP address |

## 🛑 Handling Errors

- The script includes error handling for cases like:
- Non-existent or unreachable IP addresses
- Insufficient privileges
- Graceful shutdown via keyboard interrupt (CTRL+C)

## 🛡️ Ethical Use Notice

This tool must only be used on networks you own or have been explicitly authorized to test. Unauthorized use may violate laws and regulations.
