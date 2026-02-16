import requests
import os
from dotenv import load_dotenv

load_dotenv()

def find_my_region():
    api_key = os.getenv("HENRIK_API_KEY")
    name = "spectralGaming"
    tag = "3401"
    url = f"https://api.henrikdev.xyz/valorant/v1/account/{name}/{tag}"
    
    print(f"🔍 Fetching Account Region for {name}#{tag}...")
    try:
        headers = {"Authorization": api_key} if api_key else {}
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            region = response.json()['data']['region']
            print(f"✅ SUCCESS! YOUR REGION IS: {region}")
            return region
        else:
            print(f"❌ Failed: {response.json()}")
    except Exception as e:
        print(f"⚠️ Error: {e}")
            
    print("\n😢 No region found. Please verify your PUUID in the .env file.")

if __name__ == "__main__":
    find_my_region()
