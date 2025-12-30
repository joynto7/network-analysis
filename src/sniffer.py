from scapy.all import sniff, IP, TCP, UDP, ICMP
import pandas as pd
import time
import os

timestamp = time.strftime("%Y%m%d_%H%M%S")
LOG_FILE = f"network_log_{timestamp}.csv"
PACKET_COUNT = 50

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "Other"
        
        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"
            
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"[{timestamp}] {src_ip} -> {dst_ip} | Protocol: {protocol}")
        
        log_data = {
            "Timestamp": [timestamp],
            "Source IP": [src_ip],
            "Destination IP": [dst_ip],
            "Protocol": [protocol],
            "Length": [len(packet)]
        }
        
        df = pd.DataFrame(log_data)
        
        if not os.path.isfile(LOG_FILE):
            df.to_csv(LOG_FILE, index=False, mode='w', header=True)
        else:
            df.to_csv(LOG_FILE, index=False, mode='a', header=False)

def main():
    print(f"[*] Starting NetPulse Sniffer...")
    print(f"[*] Saving logs to: {LOG_FILE}")
    print("[*] Press Ctrl+C to stop.")
    
    try:
        sniff(filter="ip", prn=packet_callback, store=0)
    except KeyboardInterrupt:
        print("\n[*] Sniffer stopped.")
    except Exception as e:
        print(f"\n[!] Error: {e}")

if __name__ == "__main__":
    main()
