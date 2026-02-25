import json
import os
from dotenv import load_dotenv
from workflow import workflow
from valorant_api import get_matches_by_player

def test_on_raw_data():
    load_dotenv()
    print("=== PIPELINE VERIFICATION TEST ===")
    
    # 1. Simulate Raw Dataset (Fetching or using sample)
    print("\n[1/3] Loading Raw Dataset...")
    region = os.getenv("VALORANT_REGION", "eu")
    puuid = os.getenv("VALORANT_PUUID", "test_player")
    
    try:
        raw_data = get_matches_by_player(region, puuid)
        print(f"✅ Loaded {len(raw_data)} raw matches.")
    except Exception as e:
        print(f"⚠️ API Error, using manual sample data: {e}")
        # Very minimal sample for fallback
        raw_data = [{
            "metadata": {"matchid": "example_123", "map": "Ascent", "game_length": 2500},
            "players": {"all_players": [{"name": "TestPlayer", "stats": {"kills": 20, "deaths": 10}}]}
        }]

    # 2. Run Workflow
    print("\n[2/3] Sending to LangChain Workflow...")
    # The workflow now returns {"status": ..., "report": ...}
    workflow_result = workflow.run(raw_data)
    result_status = workflow_result.get("status", "UNKNOWN")
    
    # 3. Retrieve and Show Cleaned Data
    print("\n[3/3] Retrieving Cleaned Result...")
    if "SUCCESSFUL" in result_status.upper():
        try:
            with open("matches_clean.csv", "r", encoding="utf-8") as f:
                print("\n--- CLEANED MATCHES (CSV Snippet) ---")
                print(f.read()[:500]) # Show first 500 chars
                
            with open("player_stats_clean.csv", "r", encoding="utf-8") as f:
                print("\n--- CLEANED PLAYER STATS (CSV Snippet) ---")
                print(f.read()[:500])
                
            print("\n✅ VERIFICATION COMPLETE: The dataset was cleaned and persisted.")
            print(f"📄 Full report saved as AAA_REPORT_FOR_USER.md")
        except Exception as e:
            print(f"❌ Error reading output: {e}")
    else:
        print(f"❌ Pipeline failed: {result_status}")

if __name__ == "__main__":
    test_on_raw_data()
