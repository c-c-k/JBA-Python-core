-- count_games_ca = "
SELECT 
  COUNT(*)
FROM
  video_games
INNER JOIN
  game_developers ON game_developers.name = video_games.game_developer
WHERE
  state = 'California'
;
-- "

-- address = "
SELECT
  address,
  state,
  city,
  country
FROM
  video_games
INNER JOIN
  game_developers ON game_developers.name = video_games.game_developer
WHERE
  state = (
    SELECT 
      state
    FROM
      video_games
    INNER JOIN
      game_developers ON game_developers.name = video_games.game_developer
    WHERE
      state IS NOT NULL
    GROUP BY
      state
    ORDER BY
      COUNT(*) DESC
    LIMIT 1
  )
ORDER BY
  release_date DESC
LIMIT 1
;
-- "
