# 🌌 Aurora Pipeline: Audit Report

> [!IMPORTANT]
> **Final Status:** ✅ SUCCESSFUL | **Execution Time:** 2026-02-24 17:32:55

## 📊 Executive Summary
⚠️ AI Audit skipped: Error calling model 'gemini-2.5-flash' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-2.5-flash\nPlease retry in 4.12977385s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel-FreeTier', 'quotaDimensions': {'model': 'gemini-2.5-flash', 'location': 'global'}, 'quotaValue': '20'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '4s'}]}}

## ⚙️ Detailed Execution Log
This section contains 100% transparent logs of every agent's input and output.

### 🤖 [Step 1] CleanerBot
- 🕒 **Time:** `17:32:52`
- 📥 **INPUT DATA:**
```json
[
  {
    "data": {
      "is_available": true,
      "metadata": {
        "map": "Sunset",
        "game_version": "release-12.02-shipping-9-4226954",
        "game_length": 724,
        "game_start": 1770840010,
        "game_start_patched": "Wednesday, February 11, 2026 08:00 PM",
        "rounds_played": 7,
        "mode": "Swiftplay",
        "mode_id": "swiftplay",
        "queue": "Swiftplay",
        "season_id": "3ea2b318-423b-cf86-25da-7cbb0eefbe2d",
        "platform": "pc",
        "matchid": "03dbe6dd-d2e7-4f28-b4f8-5324a2381e7c",
        "premier_info": {
          "tournament_id": null,
          "matchup_id": null
        },
        "region": "eu",
        "cluster": "Madrid"
      },
      "players": {
        "all_players": [
          {
            "puuid": "8130373f-cc7d-51be-896a-d4bf454ba7a4",
            "name": "Skyler",
            "tag": "G796",
            "team": "Blue",
            "level": 58,
            "character": "Sage",
            "currenttier": 0,
            "currenttier_patched": "Unrated",
            "player_card": "42d080df-41c6-4c11-ab17-948cb440bf6c",
            "player_title": "4691c456-401c-0bb5-8c31-72ab0f287b1a",
            "party_id": "87b27452-99d7-404e-bad7-80d9171145dd",
            "session_playtime": {
              "minutes": 8,
              "seconds": 480,
              "milliseconds": 480000
            },
            "behavior": {
              "afk_rounds": 0,
              "friendly_fire": {
                "incoming": 0,
                "outgoing": 0
              },
              "rounds_in_spawn": 0
            },
            "platform": {
              "type": "pc",
              "os": {
                "name": "Windows",
                "version": "10.0.19045.1.768.64bit"
              }
            },
            "ability_casts": {
              "x_cast": 0,
              "e_cast": 5,
              "q_cast": 3,
              "c_cast": 0
            },
            "assets": {
              "card": {
                "small": "https://media.valorant-api.com/playercards/42d080df-41c6-4c11-ab17-948cb440bf6c/smallart.png",
                "large": "https://media.valorant-api.com/playercards/42d080df-41c6-4c11-ab17-948cb440bf6c/largeart.png",
                "wide": "https://media.valorant-api.com/playercards/42d080df-41c6-4c11-ab17-948cb440bf6c/wideart.png"
              },
              "agent": {
                "small": "https://media.valorant-api.com/agents/569fdd95-4d10-43ab-ca70-79becc718b46/displayicon.png",
                "bust": "https://media.valorant-api.com/agents/569fdd95-4d10-43ab-ca70-79becc718b46/fullportrait.png",
                "full": "https://media.valorant-api.com/agents/569fdd95-4d10-43ab-ca70-79becc718b46/fullportrait.png",
                "killfeed": "https://media.valorant-api.com/agents/569fdd95-4d10-43ab-ca70-79becc718b46/killfeedportrait.png"
              }
            },
            "stats": {
              "score": 2080,
              "kills": 7,
   

... (truncated for report clarity)
```
- 📤 **OUTPUT PRODUCED:**
```json
[]
```

---


### 🤖 [Step 2] AnalystBot
- 🕒 **Time:** `17:32:52`
- 📥 **INPUT DATA:**
```json
[
  {
    "data": {
      "is_available": true,
      "metadata": {
        "map": "Sunset",
        "game_version": "release-12.02-shipping-9-4226954",
        "game_length": 724,
        "game_start": 1770840010,
        "game_start_patched": "Wednesday, February 11, 2026 08:00 PM",
        "rounds_played": 7,
        "mode": "Swiftplay",
        "mode_id": "swiftplay",
        "queue": "Swiftplay",
        "season_id": "3ea2b318-423b-cf86-25da-7cbb0eefbe2d",
        "platform": "pc",
        "matchid": "03dbe6dd-d2e7-4f28-b4f8-5324a2381e7c",
        "premier_info": {
          "tournament_id": null,
          "matchup_id": null
        },
        "region": "eu",
        "cluster": "Madrid"
      },
      "players": {
        "all_players": [
          {
            "puuid": "8130373f-cc7d-51be-896a-d4bf454ba7a4",
            "name": "Skyler",
            "tag": "G796",
            "team": "Blue",
            "level": 58,
            "character": "Sage",
            "currenttier": 0,
            "currenttier_patched": "Unrated",
            "player_card": "42d080df-41c6-4c11-ab17-948cb440bf6c",
            "player_title": "4691c456-401c-0bb5-8c31-72ab0f287b1a",
            "party_id": "87b27452-99d7-404e-bad7-80d9171145dd",
            "session_playtime": {
              "minutes": 8,
              "seconds": 480,
              "milliseconds": 480000
            },
            "behavior": {
              "afk_rounds": 0,
              "friendly_fire": {
                "incoming": 0,
                "outgoing": 0
              },
              "rounds_in_spawn": 0
            },
            "platform": {
              "type": "pc",
              "os": {
                "name": "Windows",
                "version": "10.0.19045.1.768.64bit"
              }
            },
            "ability_casts": {
              "x_cast": 0,
              "e_cast": 5,
              "q_cast": 3,
              "c_cast": 0
            },
            "assets": {
              "card": {
                "small": "https://media.valorant-api.com/playercards/42d080df-41c6-4c11-ab17-948cb440bf6c/smallart.png",
                "large": "https://media.valorant-api.com/playercards/42d080df-41c6-4c11-ab17-948cb440bf6c/largeart.png",
                "wide": "https://media.valorant-api.com/playercards/42d080df-41c6-4c11-ab17-948cb440bf6c/wideart.png"
              },
              "agent": {
                "small": "https://media.valorant-api.com/agents/569fdd95-4d10-43ab-ca70-79becc718b46/displayicon.png",
                "bust": "https://media.valorant-api.com/agents/569fdd95-4d10-43ab-ca70-79becc718b46/fullportrait.png",
                "full": "https://media.valorant-api.com/agents/569fdd95-4d10-43ab-ca70-79becc718b46/fullportrait.png",
                "killfeed": "https://media.valorant-api.com/agents/569fdd95-4d10-43ab-ca70-79becc718b46/killfeedportrait.png"
              }
            },
            "stats": {
              "score": 2080,
              "kills": 7,
   

... (truncated for report clarity)
```
- 📤 **OUTPUT PRODUCED:**
```json
[]
```

---


### 🤖 [Step 3] ValidatorBot (Gemini)
- 🕒 **Time:** `17:32:55`
- 📥 **INPUT DATA:**
```json
{
  "match_data": [],
  "player_stats": []
}
```
- 📤 **OUTPUT PRODUCED:**
```json
Data Validated
```

---


### 🤖 [Step 4a] Saving Matches
- 🕒 **Time:** `17:32:55`
- 📥 **INPUT DATA:**
```json
[]
```
- 📤 **OUTPUT PRODUCED:**
```json
💡 Persistence skipped: Dataset for 'matches' is empty.
```

---


### 🤖 [Step 4b] Saving Player Stats
- 🕒 **Time:** `17:32:55`
- 📥 **INPUT DATA:**
```json
[]
```
- 📤 **OUTPUT PRODUCED:**
```json
💡 Persistence skipped: Dataset for 'player_stats' is empty.
```

---


---
*Report generated by Aurora LangChain Engine v2.0*
