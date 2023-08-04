-- /*
DROP TABLE IF EXISTS video_games;
DROP TABLE IF EXISTS game_developers;
DROP TABLE IF EXISTS platforms;
DROP TABLE IF EXISTS platforms_games;
DROP TABLE IF EXISTS characters;
DROP TABLE IF EXISTS games_characters;
-- */

-- video_games_tb = "
CREATE TABLE video_games (
  id INTEGER PRIMARY KEY,
  name varchar(255) UNIQUE NOT NULL,
  game_genre varchar(255) NOT NULL,
  game_developer varchar(255) NOT NULL,
  release_date DATE NOT NULL
);
-- "

-- game_developers_tb = "
CREATE TABLE game_developers (
  id INTEGER PRIMARY KEY,
  name varchar(255) UNIQUE NOT NULL,
  address varchar(255) UNIQUE,
  state varchar(255),
  city varchar(255) NOT NULL,
  country varchar(255) NOT NULL
);
-- "

-- platforms_tb = "
CREATE TABLE platforms (
  id INTEGER PRIMARY KEY,
  name varchar(255) UNIQUE NOT NULL,
  company_id INTEGER NOT NULL,
  company NUMERIC NOT NULL,
  release_date DATETIME NOT NULL,
  original_price float NOT NULL
);
-- "

-- platforms_games_tb = "
CREATE TABLE platforms_games (
  game_id INTEGER NOT NULL,
  platform_id INTEGER NOT NULL,
  platform_name varchar(255) NOT NULL,
  PRIMARY KEY (game_id, platform_id),
  FOREIGN KEY (game_id) 
    REFERENCES video_games (id) 
      ON DELETE RESTRICT
      ON UPDATE CASCADE,
  FOREIGN KEY (platform_id) 
    REFERENCES platforms (id) 
      ON DELETE RESTRICT
      ON UPDATE CASCADE
);
-- "

-- characters_tb = "
CREATE TABLE characters (
  id INTEGER PRIMARY KEY NOT NULL,
  name varchar(255) NOT NULL,
  birthday DATETIME NOT NULL,
  gender float NOT NULL,
  info TEXT NOT NULL
);
-- "

-- games_characters_tb = "
CREATE TABLE games_characters (
  character_id INTEGER NOT NULL,
  character_name varchar(255) NOT NULL,
  game_id INTEGER NOT NULL,
  PRIMARY KEY (game_id, character_id),
  FOREIGN KEY (game_id) 
    REFERENCES video_games (id) 
      ON DELETE RESTRICT
      ON UPDATE CASCADE,
  FOREIGN KEY (character_id) 
    REFERENCES characters (id) 
      ON DELETE RESTRICT
      ON UPDATE CASCADE
);
-- "
