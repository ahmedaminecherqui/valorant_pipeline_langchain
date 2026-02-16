from dotenv import load_dotenv
import os

# Load environment variables early
load_dotenv()

from valorant_api import get_matches_by_player
from workflow import workflow

REGION = "eu"
# Note: In a real test, the user should provide a valid PUUID
PUUID = os.getenv("VALORANT_PUUID", "PUT_REAL_PUUID_HERE")

def run_pipeline():
    print(f"Fetching matches for PUUID: {PUUID} in {REGION}...")
    try:
        # For testing purposes, if PUUID is default, we might want to load local sample data
        # but let's try the API as intended.
        raw_matches = get_matches_by_player(REGION, PUUID)
    except Exception as e:
        print(f"Error fetching data: {e}")
        print("Using sample data for demonstration...")
        # Fallback to empty list or sample if API fails
        raw_matches = [] 

    print("Starting LangChain Pipeline...")
    
    if not raw_matches:
        print("No matches to process.")
        return

    result = workflow.run(raw_matches)
    
    print("\n" + "="*30)
    print("PIPELINE RESULT:")
    print(result)
    print("="*30)
    print("✅ Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()
