drop database if exists songSearch;
create database if not exists songSearch;

use songSearch;


    CREATE TABLE Songs (
      songID INT not null AUTO_INCREMENT,
      albumID INT,
      songTitle VARCHAR(50),
      albumTitle VARCHAR(50),
      length TIME,
      PRIMARY KEY (songID)
    );
   
    CREATE TABLE Albums (
      albumID INT not null auto_increment,
      artistID INT,
      albumTitle VARCHAR(50),
      artistTitle VARCHAR(50),
      genre VARCHAR(50),
      initialRelease YEAR,
      PRIMARY KEY (albumID)
    );
    
    CREATE TABLE Artists (
      artistID INT not null auto_increment,
      artistTitle VARCHAR(50),
      label VARCHAR(50), 
      PRIMARY KEY (artistID)
    );
    
    CREATE TABLE Releases (
      albumID INT,
      artistID INT,
      altYear YEAR,
      remastered BOOL,
      PRIMARY KEY (albumID, artistID)
    );
    
    CREATE TABLE Playlists (
      playlistID INT not null auto_increment,
      playlistTitle VARCHAR(50),
      PRIMARY KEY (playlistID)
    );
    
    CREATE TABLE PlaylistSongs (
      playlistID INT,
      songID INT,
      PRIMARY KEY (playlistID, songID)
    );
      
    INSERT INTO Songs(albumID, songTitle, albumTitle, length) values
    (0001, '10:15 Saturday Night', 'Three Imaginary Boys', '00:03:42'),
    (0001, 'Accuracy', 'Three Imaginary Boys', '00:02:17'),
    (0001, 'Grinding Halt', 'Three Imaginary Boys', '00:02:49'),
    (0001, 'Another Day', 'Three Imaginary Boys', '00:03:44'),
    (0001, 'Object', 'Three Imaginary Boys', '00:03:02'),
    (0001, 'Subway Song', 'Three Imaginary Boys', '00:01:58'),
    (0001, 'Foxy Lady', 'Three Imaginary Boys', '00:02:29'),
    (0001, 'Meathook', 'Three Imaginary Boys', '00:02:18'),
    (0001, 'So What', 'Three Imaginary Boys', '00:02:37'),
    (0001, 'Fire in Cairo', 'Three Imaginary Boys', '00:03:23'),
    (0001, 'It''s Not You', 'Three Imaginary Boys', '00:02:50'),
    (0001, 'Three Imaginary Boys', 'Three Imaginary Boys', '00:03:16'),
    (0001, 'The Weedy Burton', 'Three Imaginary Boys', '00:00:54'),
    (0002, 'A Reflection', 'Seventeen Seconds', '0:02:12'),
    (0002, 'Play for Today', 'Seventeen Seconds', '00:03:40'),
    (0002, 'Secrets', 'Seventeen Seconds', '00:03:40'),
    (0002, 'In Your House', 'Seventeen Seconds', '00:04:07'),
    (0002, 'Three', 'Seventeen Seconds', '00:02:36'),
    (0002, 'The Final Sound', 'Seventeen Seconds', '00:00:52'),
    (0002, 'A Forest', 'Seventeen Seconds', '00:05:54'),
    (0002, 'M', 'Seventeen Seconds', '00:03:04'),
    (0002, 'At Night', 'Seventeen Seconds', '00:05:54'),
    (0002, 'Seventeen Seconds', 'Seventeen Seconds', '00:04:00'),
    (0003, 'The Holy Hour', 'Faith', '00:04:26'),
    (0003, 'Primary', 'Faith', '00:03:39'),
    (0003, 'Other Voices', 'Faith', '00:04:23'),
    (0003, 'All Cats Are Grey', 'Faith', '00:05:27'),
    (0003, 'The Funeral Party', 'Faith', '00:04:14'),
    (0003, 'Doubt', 'Faith', '00:03:11'),
    (0003, 'The Drowning Man', '00:04:49'),
    (0003, 'Faith', 'Faith', '00:06:43'),
    (0004, 'One Hundred Years', 'Pornography', '00:06:40'),
    (0004, 'A Short Term Effect', 'Pornography', '00;04:22'),
    (0004, 'The Hanging Garden', 'Pornography', '00:04:23'),
    (0004, 'Siamese Twins', 'Pornography', '00:05:29'),
    (0004, 'The Figurehead', 'Pornography', '00:05:15'),
    (0004, 'A Strange Day', 'Pornography', '00:05:04'),
    (0004, 'Cold', 'Pornography', '00:04:26'),
    (0004, 'Pornography', 'Pornography', '00:06:27'),
    (0005, 'Shake Dog Shake', 'The Top', '00:04:58'),
    (0005, 'Bird Mad Girl', 'The Top', '00:04:05'),
    (0005, 'Wailing Wall', 'The Top', '00:05:23'),
    (0005, 'Give Me It', 'The Top', '00:03:42'),
    (0005, 'Dressing Up', 'The Top', '00:02:51'),
    (0005, 'The Caterpillar', 'The Top', '00:03:41'),
    (0005, 'Piggy in the Mirror', 'The Top', '00:03:39'),
    (0005, 'The Empty World', 'The Top', '00:02:36'),
    (0005, 'Bananafishbones', 'The Top', '00:02:59'),
    (0005, 'The Top', 'The Top', '00:06:58'),
    (0006, 'In Between Days', 'The Head on the Door', '00:02:57'),
    (0006, 'Kyoto Song', 'The Head on the Door', '00:04:15'),
    (0006, 'The Blood', 'The Head on the Door', '00:03:42'),
    (0006, 'Six Different Ways', 'The Head on the Door', '00:03:17'),
    (0006, 'Push', 'The Head on the Door', '00:04:30'),
    (0006, 'The Baby Screams', 'The Head on the Door', '00:04:30'),
    (0006, 'Close to Me', 'The Head on the Door', '00:03:22'),
    (0006, 'A Night Like This', 'The Head on the Door', '00:04:17'),
    (0006, 'Screw', 'The Head on the Door', '00:02:38'),
    (0006, 'Sinking', 'The Head on the Door', '00:04:57'),
   	(0007, 'The Kiss', 'Kiss Me, Kiss Me, Kiss Me', '00:06:16'),
   	(0007, 'Catch', 'Kiss Me, Kiss Me, Kiss Me', '00:02:44'),
    (0007, 'Torture', 'Kiss Me, Kiss Me, Kiss Me', '00:04:16'),
    (0007, 'If Only We Could Sleep', 'Kiss Me, Kiss Me, Kiss Me', '00:04:53'),
    (0007, 'Why Can''t I Be You?', 'Kiss Me, Kiss Me, Kiss Me', '00:03:13'),
    (0007, 'How Beautiful You Are...', 'Kiss Me, Kiss Me, Kiss Me', '00:05:13'),
   	(0007, 'The Snakepit', 'Kiss Me, Kiss Me, Kiss Me', '00:07:00'),
    (0007, 'Hey You!', 'Kiss Me, Kiss Me, Kiss Me', '00:02:23'),
    (0007, 'Just Like Heaven', 'Kiss Me, Kiss Me, Kiss Me', '00:03:32'),
    (0007, 'All I Want', 'Kiss Me, Kiss Me, Kiss Me', '00:05:21'),
    (0007, 'Hot Hot Hot!!!', 'Kiss Me, Kiss Me, Kiss Me', '00:03:34'),
    (0007, 'One More Time', 'Kiss Me, Kiss Me, Kiss Me', '00:04:31'),
    (0007, 'Like Cockatoos', 'Kiss Me, Kiss Me, Kiss Me', '00:03:39'),
    (0007, 'Icing Sugar', 'Kiss Me, Kiss Me, Kiss Me', '00:03:49'),
    (0007, 'The Perfect Girl', 'Kiss Me, Kiss Me, Kiss Me', '00:02:23'),
    (0007, 'A Thousand Hours', 'Kiss Me, Kiss Me, Kiss Me', '00:03:28'),
    (0007, 'Shiver and Shake', 'Kiss Me, Kiss Me, Kiss Me', '00:03:28'),
    (0007, 'Fight', 'Kiss Me, Kiss Me, Kiss Me', '00:04:31'),
    (0008, 'Plainsong', 'Disentegration', '00:05:17'),
    (0008, 'Pictures of You', 'Disentegration', '00:07:28'),
    (0008, 'Closedown', 'Disentegration', '00:04:19'),
    (0008, 'Lovesong', 'Disentegration', '00:03:29'),
    (0008, 'Last Dance', 'Disentegration', '00:04:45'),
    (0008, 'Lullaby', 'Disentegration', '00:04:09'),
    (0008, 'Fascination Street', 'Disentegration', '00:05:16'),
    (0008, 'Prayers for Rain', 'Disentegration', '00:06:08'),
    (0008, 'Same Deep Water as You', 'Disentegration', '00:09:22'),
    (0008, 'Disentegration', 'Disentegration', '00:08:21'),
    (0008, 'Homesick', 'Disentegration', '00:07:08'),
    (0008, 'Untitled', 'Disentegration', '00:06:30'),
    (0009, 'Open', 'Wish', '00:06:52'),
    (0009, 'High', 'Wish', '00:03:35'),
    (0009, 'Apart', 'Wish', '00:06:40'),
    (0009, 'From the Edge of the Deep Green Sea', 'Wish', '00:07:44'),
    (0009, 'Wendy Time', 'Wish', '00:05:33'),
    (0009, 'Doing the Unstuck', 'Wish', '00:04:24'),
    (0009, 'Friday I''m in Love', 'Wish', '00:03:39'),
    (0009, 'Trust', 'Wish', '00:05:33'),
    (0009, 'A Letter to Elise', 'Wish', '00:05:14');
    
    INSERT INTO albums(artistID, albumTitle, artistTitle, genre, initialRelease) VALUES
    (0001, 'Three Imaginary Boys', 'The Cure', 'Post-Punk', '1979'),
    (0001, 'Seventeen Seconds', 'The Cure', 'Gothic Rock', '1980'),
    (0001, 'Faith', 'The Cure', 'Gothic Rock', '1981'),
    (0001, 'Pornography', 'The Cure', 'Gothic Rock', '1982'),
    (0001, 'The Top', 'The Cure', 'Post-Punk', '1984'),
    (0001, 'The Head on the Door', 'The Cure', 'Alternative Rock', '1985'),
    (0001, 'Kiss Me, Kiss Me, Kiss Me', 'The Cure', 'Alternative Rock', '1987'),
    (0001, 'Disentegration', 'The Cure', 'Gothic Rock', '1989'),
    (0001, 'Wish', 'The Cure', 'Alternative Rock', '1992'),
    (0001, 'Show', 'The Cure', 'Alternative Rock', '1993'),
    (0001, 'Paris', 'The Cure', 'Alternative Rock', '1993'),
    (0001, 'Wild Mood Swings', 'The Cure', 'Alternative Rock', '1996'),
    (0001, 'Galore', 'The Cure', 'Alternative Rock', '1997'),
    (0001, 'Bloodflowers', 'The Cure', 'Alternative Rock', '2000'),
    (0001, 'The Cure', 'The Cure', 'Alternative Rock', '1988'),
    (0001, '4:13 Dream', 'The Cure', 'Alternative Rock', '2008');
    
    INSERT INTO Artists(artistTitle, label) VALUES
    ('The Cure', 'Fiction'),
    ('Twin Tribes', 'Twin Tribes'),
    ('London After Midnight', 'Metropolis Records'),
    ('Depeche Mode', 'Mute Records'),
    ('Sisters of Mercy', 'Merciful Release');
    
    INSERT INTO Releases(albumID, artistID, altYear, remastered) VALUES 
    (0016, 001, '2023', TRUE),
    (0020, 001, '2004', FALSE);
    
    INSERT INTO Playlists(playlistTitle) VALUES
    ('Playlist1'),
    ('Playlist2'), 
    ('Playlist3'),
    ('Playlist4'),
    ('Playlist5');
    
    INSERT INTO PlaylistSongs(playlistID, songID) VALUES
    (0001, 0003),
    (0001, 0004),
    (0001, 0012),
    (0001, 0023),
    (0001, 0008);