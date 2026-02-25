import pandas as pd
from typing import Any, Dict, List
import sqlite3
import os
from langchain_core.tools import tool
import json
import io

@tool
def match_data_cleaner(raw_matches_json: str) -> str:
    """
    Cleans and normalizes raw match-level data from the Valorant API. 
    """
    try:
        raw_matches = json.loads(raw_matches_json)
        if not isinstance(raw_matches, list):
            return json.dumps([{"error": "Input must be a list of matches", "raw": str(raw_matches)[:100]}])
            
        clean_matches = []
        for m in raw_matches:
            if not m or not isinstance(m, dict): continue
            
            # Skip if match is explicitly marked as unavailable
            if not m.get('is_available', True):
                continue

            meta = m.get('metadata') or {}
            mid = meta.get('matchid')
            # Skip records if matchid is missing or explicitly marked as unknown
            if not mid or mid == 'unknown':
                continue
            
            clean_matches.append({
                'matchid': mid,
                'map': meta.get('map', 'unknown'),
                'game_length': meta.get('game_length', 0),
                'rounds_played': meta.get('rounds_played', 0),
                'mode': meta.get('mode', 'unknown'),
                'season_id': meta.get('season_id', 'unknown')
            })
            
        df = pd.DataFrame(clean_matches)
        return df.to_json(orient='records')
    except Exception as e:
        return json.dumps([{"error": f"match_data_cleaner failed: {str(e)}"}])

@tool
def player_stats_cleaner(raw_matches_json: str) -> str:
    """
    Extracts and cleans player-specific statistics from raw Valorant match JSON data.
    """
    try:
        raw_matches = json.loads(raw_matches_json)
        if not isinstance(raw_matches, list):
            return json.dumps([{"error": "Input must be a list of matches"}])
            
        all_players = []
        for match in raw_matches:
            if not match or not isinstance(match, dict): continue
            
            # Skip if match is explicitly marked as unavailable
            if not match.get('is_available', True):
                continue

            meta = match.get('metadata') or {}
            match_id = meta.get('matchid', 'unknown')
            
            players_data = match.get('players') or {}
            player_list = players_data.get('all_players') or []
            
            for p in player_list:
                if not p: continue
                stats = p.get('stats') or {}
                all_players.append({
                    'name': p.get('name', 'Unknown'),
                    'team': p.get('team', 'Unknown'),
                    'character': p.get('character', 'Unknown'),
                    'match_id': match_id,
                    'kills': stats.get('kills', 0),
                    'deaths': stats.get('deaths', 0),
                    'assists': stats.get('assists', 0),
                    'score': stats.get('score', 0)
                })
        
        df = pd.DataFrame(all_players)
        return df.to_json(orient='records')
    except Exception as e:
        return json.dumps([{"error": f"player_stats_cleaner failed: {str(e)}"}])

@tool
def data_persistor(data_json: str, table_name: str, db_path: str = "valorant.db") -> str:
    """
    Persists cleaned JSON data into both CSV and SQLite databases.
    'table_name' will be used for both the CSV filename and the SQL table.
    """
    try:
        data = json.loads(data_json)
        if not data or (isinstance(data, list) and len(data) == 0):
            return f"💡 Persistence skipped: Dataset for '{table_name}' is empty."

        # If it's a single dict (scalar), wrap it in a list to satisfy Pandas
        if isinstance(data, dict):
            if "error" in data:
                return f"❌ Persistence failed: Source data contained an error: {data['error']}"
            data = [data]
            
        df = pd.DataFrame(data)
        
        # Save to CSV
        csv_path = f"{table_name}_clean.csv"
        df.to_csv(csv_path, index=False, encoding="utf-8")
        
        # Save to SQLite
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
        
        return f"Successfully persisted {len(df)} records to {csv_path} and table '{table_name}' in {db_path}."
    except Exception as e:
        return f"Error during persistence for {table_name}: {str(e)}"
