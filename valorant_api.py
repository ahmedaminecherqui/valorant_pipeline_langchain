import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Base URL for the Unofficual Valorant API (HenrikDev)
BASE_URL = "https://api.henrikdev.xyz/valorant"

def get_matches_by_player(region: str, puuid: str):
    """
    Fetches the 5 most recent matches for a player by PUUID from HenrikDev V3.
    Falls back to detailed sample data on error or missing API key.
    """
    api_key = os.getenv("HENRIK_API_KEY")
    url = f"{BASE_URL}/v3/by-puuid/matches/{region}/{puuid}"
    
    if api_key:
        print(f"📡 [API] Attempting LIVE fetch (Key: {api_key[:10]}...)")
        try:
            headers = {"Authorization": api_key}
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json().get('data', [])
                if data and isinstance(data, list):
                    # Filter out matches where 'is_available' is explicitly False
                    # These are stubs that often lack player/round detail
                    valid_data = [m for m in data if m.get("is_available", True)]
                    if valid_data:
                        print(f"✅ [API] Success! Fetched {len(valid_data)} playable matches (Filtered {len(data) - len(valid_data)} stubs).")
                        return valid_data
                    else:
                        print("⚠️ [API] All fetched matches were unavailable stubs.")
            
            print(f"⚠️ [API] Failed! HTTP {response.status_code}: {response.text[:100]}")
        except Exception as e:
            print(f"⚠️ [API] Connection Error: {str(e)}")
    else:
        print("💡 [INFO] HENRIK_API_KEY is empty or missing in .env. Using Mock data.")

    # High-quality Mock data for testing/fallback
    return [
        {
            "metadata": {"matchid": "m11-ascent", "map": "Ascent", "game_length": 2200, "rounds_played": 22, "mode": "Competitive"},
            "players": {"all_players": [{"name": "Sacy", "stats": {"score": 4500, "kills": 24, "deaths": 12, "assists": 8}}]}
        },
        {
            "metadata": {"matchid": "m12-bind", "map": "Bind", "game_length": 1900, "rounds_played": 18, "mode": "Competitive"},
            "players": {"all_players": [{"name": "Sacy", "stats": {"score": 3800, "kills": 18, "deaths": 14, "assists": 4}}]}
        },
        {
            "metadata": {"matchid": "m13-icebox", "map": "Icebox", "game_length": 2500, "rounds_played": 24, "mode": "Competitive"},
            "players": {"all_players": [{"name": "Sacy", "stats": {"score": 5100, "kills": 31, "deaths": 19, "assists": 12}}]}
        },
        {
            "metadata": {"matchid": "m14-haven", "map": "Haven", "game_length": 2100, "rounds_played": 21, "mode": "Unrated"},
            "players": {"all_players": [{"name": "Sacy", "stats": {"score": 2900, "kills": 15, "deaths": 8, "assists": 15}}]}
        },
        {
            "metadata": {"matchid": "m15-lotus", "map": "Lotus", "game_length": 2350, "rounds_played": 23, "mode": "Competitive"},
            "players": {"all_players": [{"name": "Sacy", "stats": {"score": 4200, "kills": 22, "deaths": 15, "assists": 9}}]}
        }
    ]
