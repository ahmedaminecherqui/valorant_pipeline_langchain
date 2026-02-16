import socket
import sys

def test_dns(hostname):
    print(f"--- Diagnosing DNS for: {hostname} ---")
    try:
        ip = socket.gethostbyname(hostname)
        print(f"✅ Success! {hostname} resolved to {ip}")
    except socket.gaierror as e:
        print(f"❌ DNS Error (getaddrinfo failed): {e}")
        print("\nPossible solutions:")
        print("1. Run 'ipconfig /flushdns' in your terminal.")
        print("2. Check if a VPN or Firewall is blocking the connection.")
        print("3. Try changing your DNS settings to 8.8.8.8 (Google) or 1.1.1.1 (Cloudflare).")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    test_dns("google.com")
    print("-" * 30)
    test_dns("api.henrikdev.xyz")
