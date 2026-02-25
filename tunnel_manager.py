import subprocess
import re
import requests
import time
import sys
import os

# CONFIGURATION
LOCAL_PORT = 8000
SUBDOMAIN = "aurora-v4-99-cherq"
# The n8n Webhook URL where we push the new tunnel URL
# Change this if your n8n address is different!
N8N_WEBHOOK_URL = "http://localhost:5678/webhook-test/update-tunnel-url" 

def start_tunnel():
    while True:
        print(f"\n🚀 [TUNNEL] Starting localtunnel on port {LOCAL_PORT}...")
        
        # Run the npx command
        cmd = ["npx", "localtunnel", "--port", str(LOCAL_PORT), "--subdomain", SUBDOMAIN]
        
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=True)

        tunnel_url = None
        
        try:
            # Read output line by line to find the URL
            for line in iter(process.stdout.readline, ""):
                if not line:
                    break
                
                print(f"📡 [LT] {line.strip()}")
                
                # Look for the URL pattern
                match = re.search(r"your url is: (https://[a-zA-Z0-9.-]+\.loca\.lt)", line)
                if match:
                    tunnel_url = match.group(1)
                    print(f"\n✅ [TUNNEL] Captured URL: {tunnel_url}")
                    sync_with_n8n(tunnel_url)
                    print(f"✨ [SYNC] Waiting for n8n requests... (Press Ctrl+C to stop everything)")

            rc = process.poll()
            if rc is not None:
                print(f"⚠️ [TUNNEL] Process exited with code {rc}. Restarting in 5s...")
                time.sleep(5)
                
        except KeyboardInterrupt:
            print("\n🛑 [TUNNEL] Stopping...")
            process.terminate()
            sys.exit(0)
        except Exception as e:
            print(f"❌ [TUNNEL] Error: {str(e)}. Restarting in 5s...")
            process.terminate()
            time.sleep(5)

def sync_with_n8n(url):
    print(f"🔄 [SYNC] Pushing URL to n8n: {N8N_WEBHOOK_URL}")
    try:
        payload = {"tunnel_url": url}
        # We use a small timeout to avoid hanging if n8n is down
        response = requests.post(N8N_WEBHOOK_URL, json=payload, timeout=5)
        
        if response.status_code == 200:
            print("🎉 [SYNC] n8n updated successfully!")
        else:
            print(f"⚠️ [SYNC] n8n responded with {response.status_code}: {response.text}")
    except Exception as e:
        print(f"❌ [SYNC] Could not connect to n8n Webhook: {str(e)}")
        print("💡 [TIP] Make sure n8n is running and the Webhook node is active.")

if __name__ == "__main__":
    start_tunnel()
