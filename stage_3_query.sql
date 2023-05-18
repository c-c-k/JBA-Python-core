-- search_nathan = "
SELECT * FROM characters WHERE name = 'Nathan Drake';
-- "

-- how_many_people = "
SELECT COUNT(*) FROM characters WHERE info LIKE '%Nathan Drake%';
-- "

-- find_location = "
SELECT address, state, city, country
FROM game_developers
WHERE name = (
  SELECT game_developer FROM video_games
  WHERE id = (
    SELECT game_id FROM games_characters 
    WHERE character_id = (
        SELECT id FROM characters WHERE name = 'Nathan Drake'
    )
  )
);
/*
SELECT
  address, state, city, country
FROM
  game_developers
INNER JOIN
  video_games ON video_games.game_developer = game_developers.name
INNER JOIN
  games_characters ON games_characters.game_id = video_games.id
INNER JOIN 
  characters ON games_characters.character_id = characters.id
WHERE
  characters.name = 'Nathan Drake'
;
*/
-- "

