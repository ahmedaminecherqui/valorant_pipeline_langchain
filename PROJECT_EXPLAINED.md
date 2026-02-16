# 🎮 Project: Valorant Insight AI
### The Complete Technical Blueprint

This document explains the "Under the Hood" mechanics of your multi-agent pipeline. It is designed to be clear, concise, and technically deep.

---

## 🏗️ 1. The Big Picture
The pipeline is a **Multi-Agent Orchestration**. Unlike a simple script, it uses LLM reasoning (Gemini) to validate and analyze data between execution steps.

- **Data Source**: Valorant Match JSON.
- **Goal**: Clean, Validate, and Persist to SQLite/CSV.
- **Engine**: LangChain + Google Gemini 2.0 Flash.

---

## 🛠️ 2. The Toolkit (`tools.py`)
These are pure Python functions decorated with `@tool`. They do the "heavy lifting".

### `match_data_cleaner`
*   **Input**: Full Raw JSON.
*   **Logic**: 
    - Uses `pandas.json_normalize` to flatten nested metadata.
    - Filters only 5 essential columns: `matchid`, `map`, `game_length`, `rounds_played`, `mode`.
*   **Output**: A clean JSON record of the match.

### `player_stats_cleaner`
*   **Logic**:
    - Iterates through the list of players.
    - Injects the `match_id` into each player record for relational mapping.
    - Flattens the `stats` nested object (Kills, Deaths, Assists).
*   **Output**: A clean JSON list of player-match performances.

### `data_persistor`
*   **Dual-Action**: Saves to CSV for humans and SQLite for applications.
*   **Logic**: Uses `df.to_sql(if_exists='replace')`.

---

## 🤖 3. The Intelligence: Agent Deep Dive (`agents.py`)

Each agent is a specialized "Expert" prompt. Here is exactly what they do and why:

### 🤖 1. CleanerBot (Match Data Expert)
*   **Role**: Handles high-level structural integrity.
*   **Tasks**:
    *   **Parsing**: Reads the complex `metadata` object from raw JSON.
    *   **Calculation**: Converts long game durations into readable minutes/seconds.
    *   **Filtering**: Strips away 90% of useless API data to keep ONLY map name, ID, and round counts.
*   **Why**: To prevent "token bloat" and ensure the database is lean.

### 🤖 2. AnalystBot (Performance Analyst)
*   **Role**: Deep-dives into individual player behavior.
*   **Tasks**:
    *   **Player Extraction**: Iterates through the `all_players` list in every match.
    *   **Stat Normalization**: Unpacks internal objects like `stats` (Kills, Deaths, Assists).
    *   **Relational Mapping**: Injects the `match_id` into every player row so you can link stats to specific games later.
*   **Why**: This is the core engine for generating personal performance reports.

### 🤖 3. ValidatorBot (Gemini Data Auditor)
*   **Role**: The AI "Brain" that ensures zero garbage enters your system.
*   **Tasks**:
    *   **Sanity Check**: Scans for "impossible" stats (e.g., negative deaths or unrealistically high ADR).
    *   **Cross-Reference**: Matches the list of players against the match ID to ensure alignment.
    *   **Format Check**: Ensures the resulting JSON is perfectly valid for the next step.
*   **Decision**: If it detects *any* anomaly, it stops the pipeline and logs the error.

### 🤖 4. Persistence Specialist (Data Engineer)
*   **Role**: Final gatekeeper for physical storage.
*   **Tasks**:
    *   **SQL Schema Sync**: Ensures the JSON data matches the SQLite table structure.
    *   **Dual-Write**: Simultaneously creates the `.csv` for Excel and the `.db` for the application.
    *   **Verification**: Only executes the commit if the previous steps returned a "Success" flag.

---

## ⚙️ 4. The Mastermind (`workflow.py`)
The `ValorantPipelineWorkflow` class coordinates the agents.

### The `run()` Trace:
1.  **Stage 1 & 2 (Parallel Concept)**:
    - CleanerBot cleans the Match info.
    - AnalystBot extracts Player stats.
2.  **Stage 3 (The Audit Gate)**:
    - The code merges the outputs.
    - Gemini (Validator) scans the result.
    - **Logic**: `if "Data Validated" in response -> proceed`.
3.  **Stage 4 (Commit)**:
    - Only if approved, `data_persistor` is called.
4.  **Stage 5 (Transparency)**:
    - Generations a full audit log in `AAA_REPORT_FOR_USER.md`.

---

## � 5. Premium Features (Why it's Robust)

*   **Transparency**:
    - Every agent input and output is logged with a timestamp in `self.history`.
*   **Terminal Aesthetics**:
    - Uses ANSI colors (`BLUE`, `GREEN`, `YELLOW`) for a pro-dev experience.
*   **Windows/OneDrive Reliability**:
    - `os.fsync()`: Forces Windows to write to disk immediately.
    - `os.startfile()`: Automatically pops up the report so you don't have to search for it.
*   **Atomic Logic**:
    - If one part fails, the whole pipeline stalls to prevent data corruption.

---

## 🛠️ 6. Extension Path
*   **Add "Performance Score"**:
    1. Define a new `@tool` in `tools.py` that calculates an OVR (Overall) score.
    2. Add a new prompt in `agents.py` for a "ScoringBot".
    3. Call it in `workflow.py` Step 2.5.
*   **Add New Maps**:
    - The cleaner is generic; it handles any new map automatically.
*   **Switch LLM**:
    - Update the `model` parameter in `agents.py` (e.g., to `gemini-1.5-pro`).
