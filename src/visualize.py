import pandas as pd
import matplotlib.pyplot as plt
import os
import glob

def generate_chart():
    log_files = glob.glob("network_log_*.csv")
    
    if not log_files:
        print("[!] Error: No 'network_log_*.csv' files found.")
        print("    Run 'sudo python src/sniffer.py' first to capture some packets!")
        return

    latest_log_file = max(log_files, key=os.path.getmtime)
    
    base_name = os.path.basename(latest_log_file)
    timestamp_part = base_name.replace("network_log_", "").replace(".csv", "")
    output_image = f"protocol_distribution_{timestamp_part}.png"

    try:
        print(f"[*] Reading data from latest log: {latest_log_file}...")
        df = pd.read_csv(latest_log_file)
        
        if df.empty:
            print("[!] The log file is empty. Capture more data.")
            return

        protocol_counts = df['Protocol'].value_counts()
        print(f"[*] Protocol counts:\n{protocol_counts}")
        
        plt.figure(figsize=(10, 6))
        plt.pie(
            protocol_counts, 
            labels=protocol_counts.index, 
            autopct='%1.1f%%', 
            startangle=140,
            shadow=True,
            colors=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']
        )
        
        plt.title(f'Network Traffic Protocol Distribution\nSource: {base_name}')
        plt.axis('equal')
        
        plt.savefig(output_image)
        print(f"[*] Chart saved successfully to: {output_image}")
        print("[*] Open the image file to view the analysis.")
        
    except pd.errors.EmptyDataError:
        print("[!] The CSV file is empty. Run sniffer.py first.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
    generate_chart()
