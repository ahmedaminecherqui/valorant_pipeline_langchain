import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_puuid(name, tag):
    api_key = os.getenv("HENRIK_API_KEY")
    url = f"https://api.henrikdev.xyz/valorant/v1/account/{name}/{tag}"
    print(f"🔍 Searching PUUID for {name}#{tag}...")
    
    try:
        headers = {"Authorization": api_key} if api_key else {}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            puuid = data['data']['puuid']
            print(f"✅ Found PUUID: {puuid}")
            return puuid
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"❌ Exception: {e}")
        return None

if __name__ == "__main__":
    name = "spectralGaming"
    tag = "3401"
    puuid = get_puuid(name, tag)
    
    if puuid:
        # Update .env file
        env_path = os.path.join(os.getcwd(), ".env")
        if os.path.exists(env_path):
            with open(env_path, 'r') as f:
                lines = f.readlines()
            
            with open(env_path, 'w') as f:
                found = False
                for line in lines:
                    if line.startswith("VALORANT_PUUID="):
                        f.write(f"VALORANT_PUUID={puuid}\n")
                        found = True
                    else:
                        f.write(line)
                if not found:
                    f.write(f"VALORANT_PUUID={puuid}\n")
            print("📝 .env file updated with the new PUUID.")
        else:
            print("⚠️ .env file not found. Please create one with VALORANT_PUUID=" + puuid)
