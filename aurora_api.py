from fastapi import FastAPI, HTTPException, Request, Query
from typing import List, Dict, Any
from workflow import workflow, BOLD, YELLOW, RESET, CYAN
from valorant_api import get_matches_by_player
import uvicorn
import json

app = FastAPI(title="Aurora Valorant Pipeline API")

@app.get("/fetch-matches")
async def fetch_matches(region: str = Query(...), puuid: str = Query(...)):
    """
    Proxy endpoint to fetch matches from HenrikDev or Mock data.
    """
    try:
        print(f"\n{BOLD}{CYAN}📡 [API] Fetching matches for {puuid} ({region})...{RESET}")
        matches = get_matches_by_player(region, puuid)
        return matches
    except Exception as e:
        print(f"❌ [API ERROR] Fetch failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/run-pipeline")
async def run_pipeline_endpoint(request: Request):
    """
    Main n8n endpoint for running the processing pipeline.
    """
    try:
        body = await request.json()
        # n8n sends data in: {"parameters": [{"name": "data", "value": [...]}]} 
        # based on aurora_n8n_workflow.json line 101. 
        # BUT n8n also often sends raw JSON if "Send Binary Data" isn't toggled.
        # Let's handle both for safety.
        
        raw_data = body
        if isinstance(body, dict) and "parameters" in body:
            # Extract from n8n parameter structure
            for param in body["parameters"]:
                if param["name"] == "data":
                    raw_data = param["value"]
                    break
        
        # If raw_data is still a list (as n8n usually passes), run it
        if not isinstance(raw_data, list):
            raw_data = [raw_data]

        print(f"\n{BOLD}{YELLOW}📡 [API] Received {len(raw_data)} matches for processing...{RESET}")
        
        # Run workflow
        workflow_result = workflow.run(raw_data)
        
        # Map 'report' to 'message' for n8n compatibility (based on .json line 139)
        workflow_result["message"] = workflow_result.get("report", "No report generated.")
        
        return workflow_result

    except Exception as e:
        print(f"❌ [API ERROR] Pipeline execution failed: {str(e)}")
        return {"status": "❌ API ERROR", "message": f"Server error: {str(e)}", "report": str(e)}

@app.post("/run")
async def run_alias(request: Request):
    """Alias for /run-pipeline for legacy support."""
    return await run_pipeline_endpoint(request)

if __name__ == "__main__":
    print(f"\n{BOLD}{YELLOW}🚀 Aurora API starting on http://localhost:8000{RESET}")
    print(f"{CYAN}Endpoints: /fetch-matches (GET), /run-pipeline (POST){RESET}\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)
