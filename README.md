# ARP Spoofing Tool

This repository contains a Python script for performing ARP spoofing attacks. 

**Disclaimer:**

* ARP spoofing is a powerful technique that can be used for both ethical and malicious purposes. 
* Using this script for any unauthorized activity is strictly prohibited and may be illegal. 
* This script is provided for educational purposes only and should be used responsibly and ethically.

**Features:**

* Spoofs ARP traffic between a target and its gateway.
* Restores ARP tables upon interruption.
* Includes basic argument parsing for user-friendly input.

**Usage:**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Gaurav909565/ARP_Spoofer.git
   ```

2. **Navigate to the repository:**
   ```bash
   cd ARP_Spoofer/
   ```

3. **Run the script:**
   ```bash
   python arp_spoofer.py -t <target_ip> -g <gateway_ip> -i <interface>
   ```
   * **-t, --target:** Specify the IP address of the target device.
   * **-g, --gateway:** Specify the IP address of the gateway.
   * **-i, --interface:** Specify the network interface to use for the attack.

**Example:**

```bash
python arp_spoofer.py -t 192.168.1.100 -g 192.168.1.1 -i eth0
```

This will start an ARP spoofing attack on the target with IP address 192.168.1.100 and the gateway with IP address 192.168.1.1 using the eth0 interface.

**Note:**

* This script requires the Scapy library. Install it using:
   ```bash
   pip install scapy
   ```
* This script is designed for educational purposes only and should not be used for any unauthorized activities. 
* The user is solely responsible for any consequences arising from the use of this script.

**Disclaimer:**

This tool is for educational and ethical purposes only. The developer is not responsible for any misuse of this tool. Using this tool for illegal activities is strictly prohibited.

This README provides a clear and concise description of the ARP spoofing script, including its purpose, usage instructions, disclaimer, and ethical considerations. It also includes instructions on how to clone the repository and install the required library.
