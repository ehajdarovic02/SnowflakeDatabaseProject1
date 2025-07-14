
SELECT game_name, tag_line, number_of_wins
FROM LEADERBOARD
ORDER BY number_of_wins DESC
LIMIT 10;

SELECT game_name, tag_line, leaderboard_rank, number_of_wins
FROM leaderboard
ORDER BY leaderboard_rank ASC
LIMIT 10;

SELECT rankedRating, COUNT(*) AS players
FROM leaderboard
GROUP BY competitive_tier
ORDER BY players DESC;

SELECT 
    game_name,
    rankedRating,
    number_of_wins,
    CASE 
        WHEN number_of_wins > 0 THEN ROUND(rankedRating / number_of_wins, 2)
        ELSE NULL
    END AS rr_per_win
FROM leaderboard
ORDER BY rr_per_win DESC;


SELECT 
    game_name, 
    leaderboard_rank, 
    rankedRating, 
    number_of_wins
FROM leaderboard
ORDER BY rankedRating DESC;


SELECT 
    CASE 
        WHEN number_of_wins < 50 THEN '0–49 wins'
        WHEN number_of_wins < 100 THEN '50–99 wins'
        WHEN number_of_wins < 150 THEN '100–149 wins'
        ELSE '150+ wins'
    END AS win_bracket,
    COUNT(*) AS players,
    ROUND(AVG(rankedRating), 2) AS avg_rating
FROM leaderboard
GROUP BY win_bracket
ORDER BY win_bracket;

