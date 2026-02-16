import pandas as pd
import sqlite3
import os

def inspect_results():
    db_path = "valorant.db"
    csv_matches = "matches_clean.csv"
    csv_stats = "player_stats_clean.csv"
    
    print("=== FINAL DATASET PERSISTENCE CHECK ===\n")
    
    # Check Files
    for f in [db_path, csv_matches, csv_stats]:
        if os.path.exists(f):
            print(f"✅ Found: {f} ({os.path.getsize(f)} bytes)")
        else:
            print(f"❌ Missing: {f}")
            
    print("\n--- Content Summary (CSV) ---")
    if os.path.exists(csv_matches):
        df_m = pd.read_csv(csv_matches)
        print(f"Matches CSV: {len(df_m)} rows. Columns: {list(df_m.columns)}")
        print(df_m.head(2))
        
    if os.path.exists(csv_stats):
        df_s = pd.read_csv(csv_stats)
        print(f"\nPlayer Stats CSV: {len(df_s)} rows. Columns: {list(df_s.columns)}")
        print(df_s.head(5))

    print("\n--- Database Check (SQLite) ---")
    if os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"Tables in DB: {[t[0] for t in tables]}")
        
        for table in tables:
            count = pd.read_sql_query(f"SELECT COUNT(*) as count FROM {table[0]}", conn)['count'][0]
            print(f" - Table '{table[0]}': {count} records")
        conn.close()

if __name__ == "__main__":
    inspect_results()
