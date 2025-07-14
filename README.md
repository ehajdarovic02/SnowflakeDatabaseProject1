This project is a data analysis pipeline that leverages the Riot Games official API for the game Valorant. The system retrieves data through API calls, organizes it into structured datasets, and performs insightful analysis using SQL queries.

Overview
API Integration: Connects to Riot Games’ official Valorant API to fetch player and match data.

Data Storage: Collected data is stored in structured datasets using Snowflake.

SQL Analysis: Uses SQL queries to analyze trends, player performance, and other game-related metrics.

Features
- Fetch player statistics and match history
- Store raw and cleaned data for future use
- Run custom SQL queries for advanced insights
- Scalable setup for future expansion (e.g., leaderboard generation, predictive modeling)

Requirements
- Python 3.x
- SQL engine
- Riot Games Developer API Key (https://developer.riotgames.com)
