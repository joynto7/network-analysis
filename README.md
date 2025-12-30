#  Network Traffic Analyzer & Visualizer

A Python-based cybersecurity tool that captures live network packets, logs them into a structured format, and provides visual analytics of network protocols.

## 🚀 Overview
THis project designed to provide visibility into local network traffic. By putting the network interface into **Promiscuous Mode**, it "listens" to passing data, dissects IP headers, and identifies protocols like TCP, UDP, and ICMP.

### Key Features
* **Real-time Sniffing:** Live console output of source/destination IPs and protocols.
* **Data Logging:** Automatically saves session data to `network_log.csv` for forensic analysis.
* **Visual Analytics:** Generates distribution charts (Pie charts) of network protocols using Matplotlib.
* **Security Focused:** Designed as a lightweight tool for learning Network Forensics and the OSI Model.

---

## 🛠️ Setup & Installation

### Prerequisites
* **Python 3.x**
* **Npcap (Windows)** or **libpcap (Mac/Linux)**: Required for raw packet capturing.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/network-analysis.git
   cd network-analysis
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚦 How to Run

### 1. Start the Sniffer

**Note:** You must run this with Administrator/Sudo privileges.

```bash
# Linux/Mac
sudo python src/sniffer.py

# Windows (Run VS Code as Admin)
python src/sniffer.py
```

### 2. Generate Visualizations

After capturing some data, run the visualizer to see the protocol breakdown:

```bash
python src/visualize.py
```

---

