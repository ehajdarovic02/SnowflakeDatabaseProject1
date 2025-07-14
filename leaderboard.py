import requests
import snowflake.connector
import os
import json

# --- API Setup ---
RIOT_API_KEY='RGAPI-54541f58-5491-4748-9344-d6434014a1be'
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": RIOT_API_KEY}
ACT_ID = "dcde7346-4085-de4f-c463-2489ed47983b"

url = f"https://na.api.riotgames.com/val/ranked/v1/leaderboards/by-act/{ACT_ID}?size=100&startIndex=0"
response = requests.get(url, headers=HEADERS)
data = response.json()

players = data["players"]

# --- Snowflake Connection ---
conn = snowflake.connector.connect(
    user="elizahaj",
    password="g29cXRw6F-_N!Dr",
    account="ETYSSZO-RIC87281",
    warehouse="COMPUTE_WH",
    database="VALORANT_DB",
    schema="PUBLIC"
)
cursor = conn.cursor()

# --- Create Table ---
cursor.execute("""
    CREATE OR REPLACE TABLE leaderboard (
        puuid STRING,
        game_name STRING,
        tag_line STRING,
        leaderboard_rank INT,
        rankedRating INT,
        number_of_wins INT,
        competitive_tier INT
    )
""")

# --- Insert Data ---
for p in players:
    cursor.execute("""
        INSERT INTO leaderboard VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        p.get('puuid'),
        p.get('gameName'),
        p.get('tagLine'),
        p.get('leaderboardRank', 0),
        p.get("rankedRating",0),
        p.get('numberOfWins', 0),
        p.get('competitiveTier', 0)
    ))

cursor.close()
conn.close()
