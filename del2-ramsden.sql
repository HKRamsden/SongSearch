drop database if exists songSearch;
create database if not exists songSearch;

use songSearch;


    CREATE TABLE Songs (
      songID INT,
      albumID INT,
      songTitle VARCHAR(50),
      albumTitle VARCHAR(50),
      length TIME,
      PRIMARY KEY (songID, albumID)
    );
    
    CREATE TABLE Albums (
      albumID INT,
      artistID INT,
      albumTitle VARCHAR(50),
      artistTitle VARCHAR(50),
      genre VARCHAR(50),
      initialRelease YEAR,
      PRIMARY KEY (albumID)
    );
    
    CREATE TABLE Artists (
      artistID INT,
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
      playlistID INT,
      playlistTitle VARCHAR(50),
      PRIMARY KEY (playlistID)
    );
    
    CREATE TABLE PlaylistSongs (
      playlistID INT,
      songID INT,
      albumID INT,
      PRIMARY KEY (playlistID, songID, albumID)
    );
      
    INSERT INTO Songs (songID, albumID, songTitle, albumTitle, length) VALUES
    (0001, 0008, 'In Between Days', 'The Head on the Door', '00:02:57'),
    (0002, 0008, 'Kyoto Song', 'The Head on the Door', '00:04:15'),
    (0003, 0008, 'The Blood', 'The Head on the Door', '00:03:42'),
    (0004, 0008, 'Six Different Ways', 'The Head on the Door', '00:03:17'),
    (0005, 0008, 'Push', 'The Head on the Door', '00:04:30'),
    (0006, 0008, 'The Baby Screams', 'The Head on the Door', '00:04:30'),
    (0007, 0008, 'Close to Me', 'The Head on the Door', '00:03:22'),
    (0008, 0008, 'A Night Like This', 'The Head on the Door', '00:04:17'),
    (0009, 0008, 'Screw', 'The Head on the Door', '00:02:38'),
    (0010, 0008, 'Sinking', 'The Head on the Door', '00:04:57');
    
    INSERT INTO albums VALUES
    (0001, 0001, 'Three Imaginary Boys', 'The Cure', 'Post-Punk', '1979'),
    (0002, 0001, 'Boys Don''t Cry', 'The Cure', 'Post-Punk', '1980'),
    (0003, 0001, 'Seventeen Seconds', 'The Cure', 'Gothic Rock', '1980'),
    (0004, 0001, 'Faith', 'The Cure', 'Gothic Rock', '1981'),
    (0005, 0001, 'Pornography', 'The Cure', 'Gothic Rock', '1982'),
    (0006, 0001, 'Japanese Whispers', 'The Cure', 'New Wave', '1983'),
    (0007, 0001, 'The Top', 'The Cure', 'Post-Punk', '1984'),
    (0008, 0001, 'The Head on the Door', 'The Cure', 'Alternative Rock', '1985'),
    (0009, 0001, 'Standing on a Beach/Staring at the Sea', 'The Cure', 'Alternative Rock', '1986'),
    (0010, 0001, 'Kiss Me, Kiss Me, Kiss Me', 'The Cure', 'Alternative Rock', '1987'),
    (0011, 0001, 'Disentegration', 'The Cure', 'Gothic Rock', '1989'),
    (0012, 0001, 'Mixed Up', 'The Cure', 'Alternative Rock', '1990'),
    (0013, 0001, 'Entreat', 'The Cure', 'Gothic Rock', '1991'),
    (0014, 0001, 'Wish', 'The Cure', 'Alternative Rock', '1992'),
    (0015, 0001, 'Show', 'The Cure', 'Alternative Rock', '1993'),
    (0016, 0001, 'Paris', 'The Cure', 'Alternative Rock', '1993'),
    (0017, 0001, 'Wild Mood Swings', 'The Cure', 'Alternative Rock', '1996'),
    (0018, 0001, 'Galore', 'The Cure', 'Alternative Rock', '1997'),
    (0019, 0001, 'Bloodflowers', 'The Cure', 'Alternative Rock', '2000'),
    (0020, 0001, 'The Cure', 'The Cure', 'Alternative Rock', '1988'),
    (0021, 0001, '4:13 Dream', 'The Cure', 'Alternative Rock', '2008');
    
    INSERT INTO Artists(artistID, artistTitle, label) VALUES
    (0001, 'The Cure', 'Fiction'),
    (0002, 'Twin Tribes', 'Twin Tribes'),
    (0003, 'London After Midnight', 'Metropolis Records'),
    (0004, 'Depeche Mode', 'Mute Records'),
    (0005, 'Sisters of Mercy', 'Merciful Release');
    
    INSERT INTO Releases(albumID, artistID, altYear, remastered) VALUES 
    (0016, 001, '2023', TRUE),
    (0020, 001, '2004', FALSE);
    
    INSERT INTO Playlists(playlistID, playlistTitle) VALUES
    (0001, 'Playlist1'),
    (0002, 'Playlist2'), 
    (0003, 'Playlist3'),
    (0004, 'Playlist4'),
    (0005, 'Playlist5');
    
    INSERT INTO PlaylistSongs(playlistID, songID, albumID) VALUES
    (0001, 0003, 0008),
    (0001, 0004, 0008),
    (0002, 0012, 0008),
    (0004, 0003, 0008),
    (0003, 0008, 0008);