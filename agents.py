from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from tools import match_data_cleaner, player_stats_cleaner, data_persistor

# Initialize the LLM (Gemini)
# Standard models: 'gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-2.0-flash', 'gemini-2.5-flash'
# Using 'gemini-flash-latest' as it's verified to work with your API key configuration
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0, 
    max_retries=1,
    request_timeout=120
)

# 1. Match Data Cleaning Agent (using tool directly via LCEL or functional call)
# Since the user wants to test the workflow easily, we'll expose components that can be chained.

match_cleaner_prompt = ChatPromptTemplate.from_template(
    "You are a Valorant Match Data Expert. Your goal is to clean raw match data.\n"
    "Raw Data: {raw_data}\n"
    "Use the match_data_cleaner tool to process this data."
)

player_stats_prompt = ChatPromptTemplate.from_template(
    "You are a Valorant Player Performance Analyst. Your goal is to extract and clean player stats.\n"
    "Raw Data: {raw_data}\n"
    "Use the player_stats_cleaner tool to process this data."
)

validator_prompt = ChatPromptTemplate.from_template(
    "You are a Data Quality Auditor. Review the following cleaned JSON data for technical consistency.\n"
    "Data: {cleaned_data}\n"
    "Focus on: 1. Valid structure, 2. No 'unknown' placeholders in critical fields, 3. Matching IDs between datasets.\n"
    "DO NOT reject data based on poor player performance (bad stats are valid data).\n"
    "If technically sound, respond with ONLY the phrase 'Data Validated'. If not, concisely describe the technical issues."
)

persistence_prompt = ChatPromptTemplate.from_template(
    "You are a Data Engineer. Persist the following cleaned JSON data to SQLite and CSV.\n"
    "Table Name: {table_name}\n"
    "Data: {data_json}\n"
    "Use the data_persistor tool."
)

reporter_prompt = ChatPromptTemplate.from_template(
    "You are 'ReportSage', an Elite System Auditor. Your goal is a stunning, transparent Markdown report.\n\n"
    "REPORT STRUCTURE:\n"
    "1. # 🌌 Aurora Pipeline: Audit Report (Large Heading)\n"
    "2. ## 📊 Execution Summary (Status table with 🟢/🔴 icons)\n"
    "3. ## ⚙️ Agent Log (Detailed breakdown)\n\n"
    "FOR EVERY STEP IN THE HISTORY:\n"
    "- ### 🤖 [Step {step}] {agent}\n"
    "- **Execution Time:** {timestamp}\n"
    "- **📥 INPUT RECEIVED:**\n"
    "```json\n"
    "{{input}}\n"
    "```\n"
    "- **📤 OUTPUT PRODUCED:**\n"
    "```json\n"
    "{{output}}\n"
    "```\n"
    "--- (Visual divider)\n\n"
    "GUIDELINES:\n"
    "- Do NOT skip agents. Do NOT summarize.\n"
    "- Use emojis to make it feel premium and modern.\n\n"
    "EXECUTION HISTORY:\n"
    "{history_data}\n\n"
    "FINAL STATUS: {final_status}\n\n"
    "Generate the PERFECT report now."
)
