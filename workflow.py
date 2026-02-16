import json
import os
from datetime import datetime
import traceback
from agents import validator_prompt, llm
from tools import match_data_cleaner, player_stats_cleaner, data_persistor

# ANSI Colors for Terminal Beautification
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

class ValorantPipelineWorkflow:
    def __init__(self):
        self.llm = llm
        self.history = []

    def _log_agent(self, step: str, name: str, input_data: str, output_data: str):
        """Helper to log steps in history and console with BEAUTIFUL truncation and JSON formatting."""
        
        def console_beautify(data_str, limit=1000):
            try:
                # Attempt to parse as JSON for pretty printing
                parsed = json.loads(data_str)
                # If it's a huge list, just show the first item and the count
                if isinstance(parsed, list) and len(parsed) > 1:
                    header = f"📋 [List of {len(parsed)} items]"
                    pretty = json.dumps(parsed[0], indent=2)
                    return f"{header}\n{pretty}\n... (+{len(parsed)-1} more records)"
                return json.dumps(parsed, indent=2)
            except:
                # If not JSON, just return truncated string
                s = str(data_str)
                return s[:limit] + ("..." if len(s) > limit else "")

        # Console Output
        print(f"\n{BOLD}{MAGENTA}🤖 [STEP {step}] {name.upper()}{RESET}")
        print(f"{CYAN}📥 INPUT RECEIVED:{RESET}\n{BOLD}{console_beautify(input_data, 300)}{RESET}")
        print(f"{GREEN}📤 OUTPUT PRODUCED:{RESET}\n{BOLD}{console_beautify(output_data, 800)}{RESET}")
        print(f"{YELLOW}{'═'*60}{RESET}")

        # Truncate for report history if too large (> 5000 chars)
        # We keep the raw data in history for the report, but truncate only if insane
        r_input = input_data if len(input_data) < 10000 else input_data[:10000] + "\n... [TRUNCATED] ..."
        r_output = output_data if len(output_data) < 10000 else output_data[:10000] + "\n... [TRUNCATED] ..."

        self.history.append({
            "step": step,
            "agent": name,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "input": r_input,
            "output": r_output
        })

    def generate_report(self, final_status: str):
        """Writes the execution history to a Markdown file in guaranteed locations."""
        report_filename = "AAA_REPORT_FOR_USER.md"
        
        # 1. Path relative to the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        path_script = os.path.join(script_dir, report_filename)
        
        # 2. Path in the current working directory (where the user is)
        path_cwd = os.path.join(os.getcwd(), report_filename)
        
        target_paths = list(set([path_script, path_cwd])) # Avoid duplicate writes if same
        
        for p in target_paths:
            try:
                with open(p, "w", encoding="utf-8") as f:
                    f.write(f"# 📊 Valorant Pipeline Execution Report\n\n")
                    f.write(f"- **Generated on:** `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`\n")
                    f.write(f"- **Final Result:** **{final_status}**\n\n")
                    f.write(f"## 🛠️ Step-by-Step Agent Audit\n\n")
                    
                    for entry in self.history:
                        f.write(f"### 🤖 Step {entry['step']}: {entry['agent']}\n")
                        f.write(f"- **Timestamp:** `{entry['timestamp']}`\n")
                        
                        try:
                            pretty_in = json.dumps(json.loads(entry['input']), indent=2)
                        except: pretty_in = entry['input']
                        
                        try:
                            pretty_out = json.dumps(json.loads(entry['output']), indent=2)
                        except: pretty_out = entry['output']

                        f.write(f"#### 📥 Input Received\n```json\n{pretty_in}\n```\n")
                        f.write(f"#### 📤 Output Produced\n```json\n{pretty_out}\n```\n")
                        f.write("\n---\n")
                    
                    f.flush()
                    os.fsync(f.fileno())
            except Exception as e:
                print(f"{RED}⚠️ Could not write to {p}: {e}{RESET}")

        # Super clear output and debug check
        print(f"\n{BOLD}{YELLOW}╔════════════════════════════════════════════════════════════════╗{RESET}")
        print(f"{BOLD}{YELLOW}║ 📄 REPORT GENERATED: {report_filename.upper():<37} ║{RESET}")
        print(f"{BOLD}{YELLOW}╚════════════════════════════════════════════════════════════════╝{RESET}")
        
        # Force open the file on Windows
        try:
            os.startfile(path_script)
            print(f"{GREEN}🚀 FORCING OPEN:{RESET} {path_script}")
        except: pass

        print(f"{BOLD}Location:{RESET} {path_script}")
        print(f"{CYAN}Open Link:{RESET} file:///{path_script.replace(os.sep, '/')}\n")

    def run(self, raw_matches: list):
        self.history = [] # Reset history
        raw_matches_json = json.dumps(raw_matches)

        print("\n" + "═"*60)
        print(f"{BOLD}{YELLOW}🚀 STARTING ENHANCED MULTI-AGENT PIPELINE{RESET}")
        print("═"*60)

        # STEP 1: CLEANING
        cleaned_matches_json = match_data_cleaner.invoke({"raw_matches_json": raw_matches_json})
        print(f"🔍 [DEBUG] CleanerBot output (first 50 chars): {str(cleaned_matches_json)[:50]}")
        self._log_agent("1", "CleanerBot", raw_matches_json, cleaned_matches_json)
        
        # STEP 2: ANALYST
        cleaned_player_stats_json = player_stats_cleaner.invoke({"raw_matches_json": raw_matches_json})
        self._log_agent("2", "AnalystBot", raw_matches_json, cleaned_player_stats_json)

        # STEP 3: VALIDATOR
        def safe_json_load(data_str, bot_name):
            try:
                # Basic check: if it doesn't start with { or [, it's likely an error string
                cleaned_str = data_str.strip()
                if not (cleaned_str.startswith("{") or cleaned_str.startswith("[")):
                    return {"error": f"Bot {bot_name} did not return JSON.", "raw_output": data_str[:200]}
                return json.loads(cleaned_str)
            except Exception as e:
                # Modified to include traceback for better debugging
                return {"error": f"Failed to parse {bot_name} JSON: {str(e)}\nTraceback: {traceback.format_exc()}", "raw_output": data_str[:200]}

        validation_input = json.dumps({
            "match_data": safe_json_load(cleaned_matches_json, "CleanerBot"), 
            "player_stats": safe_json_load(cleaned_player_stats_json, "AnalystBot")
        }, indent=2)
        
        validation_response = (validator_prompt | self.llm).invoke({"cleaned_data": validation_input})
        val_content = validation_response.content
        self._log_agent("3", "ValidatorBot (Gemini)", validation_input, val_content)

        if "data validated" in val_content.lower():
            # STEP 4: PERSISTENCE
            print(f"\n{BOLD}{CYAN}🤖 [STEP 4] Persistence Specialist...{RESET}")
            res1 = data_persistor.invoke({"data_json": cleaned_matches_json, "table_name": "matches"})
            res2 = data_persistor.invoke({"data_json": cleaned_player_stats_json, "table_name": "player_stats"})
            
            self._log_agent("4a", "Saving Matches", cleaned_matches_json, res1)
            self._log_agent("4b", "Saving Player Stats", cleaned_player_stats_json, res2)

            if "Error" in res1 or "Error" in res2:
                final_status = "⚠️ COMPLETED WITH ERRORS"
            else:
                final_status = "✅ SUCCESSFUL"
        else:
            final_status = f"❌ STALLED AT VALIDATION"

        self.generate_report(final_status)
        print("═"*60 + "\n")
        return final_status

workflow = ValorantPipelineWorkflow()
