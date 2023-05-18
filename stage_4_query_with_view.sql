-- count_games_ca = "
DROP VIEW IF EXISTS games_with_developer_info;
CREATE VIEW games_with_developer_info
AS
SELECT 
  video_games.release_date AS game_release_date,
  game_developers.name AS developer_name,
  game_developers.address AS developer_address,
  game_developers.state AS developer_state,
  game_developers.city AS developer_city,
  game_developers.country AS developer_country
FROM
  video_games
INNER JOIN
  game_developers ON game_developers.name = video_games.game_developer
;

SELECT 
  COUNT(*)
FROM
  games_with_developer_info
WHERE
  developer_state = 'California'
;
-- "

-- address = "
SELECT
  developer_address,
  developer_state,
  developer_city,
  developer_country
FROM
  games_with_developer_info
WHERE
  developer_state = (
    SELECT 
      developer_state
    FROM
      games_with_developer_info
    WHERE
      developer_state IS NOT NULL
    GROUP BY
      developer_state
    ORDER BY
      COUNT(developer_state) DESC
    LIMIT 1
)
ORDER BY
  game_release_date DESC
LIMIT 1
;
-- "
