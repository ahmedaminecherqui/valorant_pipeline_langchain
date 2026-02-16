# Valorant Data Pipeline

A LangChain-powered data ingestion pipeline that fetches, cleans, validates, and persists Valorant match data using the HenrikDev API.

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- A Google API key (for Gemini LLM)
- A HenrikDev API key ([Get one here](https://docs.henrikdev.xyz/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ahmedaminecherqui/valorant_pipeline_langchain.git
   cd valorant_pipeline_langchain
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   HENRIK_API_KEY=your_henrik_api_key_here
   VALORANT_PUUID=your_player_puuid
   VALORANT_REGION=eu
   ```

   > **Note:** If you don't know your PUUID or region, use the utility scripts in `tests/`:
   > ```bash
   > python tests/get_my_puuid.py
   > python tests/find_region.py
   > ```

### Running the Pipeline

**Option 1: Full Test Pipeline (Recommended)**
```bash
python test_pipeline.py
```
This will:
- Fetch your last 5 matches from the API
- Clean and validate the data using LangChain agents
- Persist data to CSV and SQLite
- Generate a detailed execution report (`AAA_REPORT_FOR_USER.md`)
- Display results in the terminal

**Option 2: Simple Entry Point**
```bash
python main.py
```
A simpler version without detailed reporting.

## 📁 Project Structure

```
valorant_pipeline_langchain/
├── agents.py              # LangChain agent definitions (CleanerBot, AnalystBot, ValidatorBot)
├── tools.py               # Data cleaning & persistence tools
├── workflow.py            # Pipeline orchestration logic
├── valorant_api.py        # HenrikDev API integration
├── main.py                # Simple entry point
├── test_pipeline.py       # Comprehensive testing entry point
├── tests/                 # Utility scripts
│   ├── find_region.py     # Detect your Valorant region
│   ├── get_my_puuid.py    # Fetch your player PUUID
│   ├── test_connexion.py  # Test API connectivity
│   ├── test_gemini.py     # Test Gemini LLM
│   └── verify_data.py     # Verify generated data
└── requirements.txt       # Python dependencies
```

## 📊 Output Files

After running the pipeline, you'll find:

- **`matches_clean.csv`** - Cleaned match metadata (map, mode, duration, etc.)
- **`player_stats_clean.csv`** - Player statistics (kills, deaths, assists, score)
- **`valorant.db`** - SQLite database with both tables
- **`AAA_REPORT_FOR_USER.md`** - Detailed execution report with agent logs

## 🛠️ Troubleshooting

### API Connection Issues
```bash
python tests/test_connexion.py
```

### Region Detection Problems
```bash
python tests/find_region.py
```

### Verify Generated Data
```bash
python tests/verify_data.py
```

## 📖 Documentation

- **[PROJECT_EXPLAINED.md](PROJECT_EXPLAINED.md)** - Detailed project overview
- **[WORKFLOW_EXPLAINED.md](WORKFLOW_EXPLAINED.md)** - Pipeline workflow explanation

## 🔑 API Keys

- **Google API Key**: Get from [Google AI Studio](https://makersuite.google.com/app/apikey)
- **HenrikDev API Key**: Get from [HenrikDev Dashboard](https://docs.henrikdev.xyz/)

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
