from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from tools import match_data_cleaner, player_stats_cleaner, data_persistor

# Initialize the LLM (Gemini)
# Standard models: 'gemini-1.5-flash', 'gemini-1.5-pro'
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

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
