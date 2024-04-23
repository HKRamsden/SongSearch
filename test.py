###### Imports #####
from tkinter import * 
import mariadb as sql


##### Database connection #####
def connect_to_database():
    try:
        db = sql.connect(host = 'localhost',
                         user = 'root',
                         password = 'root',
                         database = 'songSearch')
        return db
    except sql.Error as error:
        print("Error connecting to database: ", error)
        return None

def test_create(db):
    cursor = db.cursor()
    query = 'SELECT * FROM PlaylistSongs'
    cursor.execute(query)
    result = cursor.fetchall()
    print(query)
    for songs in result:
        print(songs)
    print()

def main():
    db = connect_to_database()
    if db == None:
        print("No Database")
        return 
    test_create(db)
    
if __name__ == "__main__":
    main()


### UI SECTION ###

##### Creating Windows #####
root = Tk()

##### Saving color codes #####
bkgndColor = "#AB7CF2"
mainColor = "#9265d6"
acctColor = "#472c70"

# root window title and dimension #
root.title("SongSearch - Welcome!")
# set geometry (w x h) #
root.geometry('1000x1000')
# set background color #
root.configure(bg=bkgndColor)

##### Creating Frames in the Window #####
startPage = Frame(root)
songPage = Frame(root)
playlistPage = Frame(root)

##### Setting background colors for each frame #####
startPage.configure(bg=bkgndColor)
songPage.configure(bg=bkgndColor)
playlistPage.configure(bg=bkgndColor)

### Defining Variables for text input ###
searchTextPlay = StringVar()
searchTextSong = StringVar()
enterPlaylistName = StringVar()
searchArtist = StringVar()
searchAlbum = StringVar()
searchSong = StringVar()
searchRelease = StringVar()

##### Setting Labels for each frame #####
## Start Page ##
startLabel = Label(startPage, text = "Welcome to SongSearch!", font="Arial 20 bold", bg=bkgndColor, fg=acctColor)
startLabel.place(relx = 1, rely=0, anchor='ne')

## Song Page ##
songLabel = Label(songPage, text = "Song Management", font = "Arial 20 bold", bg=bkgndColor, fg=acctColor)
songLabel.place(relx = 1, rely = 0, anchor = 'ne')

## Playlist Page ##
playlistLabel = Label(playlistPage, text = "Playlist Management", font = "Arial 20 bold", bg=bkgndColor, fg=acctColor)
playlistLabel.place(relx=1, rely=0, anchor='ne')

##### Change Frames Commands #####
## Start Page ##
def change_to_start():
    startPage.pack(fill = 'both', expand = 1)
    songPage.pack_forget()
    playlistPage.pack_forget()

## Song Page ##
def change_to_song():
    songPage.pack(fill = 'both', expand = 1)
    startPage.pack_forget()
    playlistPage.pack_forget()
    startLabel.pack_forget()

## Playlist Page ##
def change_to_playlist():
    playlistPage.pack(fill='both', expand = 1)
    startPage.pack_forget()
    songPage.pack_forget()
    startLabel.pack_forget()
    
##### Setting up initial page #####
# button borders
mpButtonBorder = Frame(startPage, highlightbackground = mainColor, highlightthickness = 5, bd = 0)
msButtonBorder = Frame(startPage, highlightbackground = mainColor, highlightthickness = 5, bd = 0)
startButtonBorder = Frame(root, highlightbackground = mainColor, highlightthickness = 5, bd = 0)
# Adding Main Menu Button
startButtonBorder.place(relx = 0, rely = 0)

startButton = Button(startButtonBorder, 
                     text = "Main menu", 
                     font = "Arial 15", 
                     fg=acctColor, 
                     bg=bkgndColor, 
                     width=15, 
                     height=2, 
                     command = change_to_start)
startButton.pack()

# Adding in Manage Playlist button 
mpButtonBorder.place(relx = 0.2, rely = 0)
mpButton = Button(mpButtonBorder, 
                  text = "Manage Playlists", 
                  font = "Arial 15", 
                  fg=acctColor, 
                  bg=bkgndColor, 
                  width=15, 
                  height=2,
                  command = change_to_playlist)
mpButton.pack()

# Adding in Manage Songs button
msButtonBorder.place(relx = 0.4, rely= 0)
msButton = Button(msButtonBorder, 
                  text = "Manage Songs", 
                  font = "Arial 15", 
                  fg = acctColor, 
                  bg = bkgndColor, 
                  width = 15, 
                  height = 2,
                  command=change_to_song)
msButton.pack()

##### Playlist Window #####

### Creating Pop Up Windows ###
def openAdPlayWindow():
    adPlayWindow = Toplevel(root)
    adPlayWindow.configure(bg = mainColor)
    adPlayWindow.title("Add / Delete Playlists")
    adPlayWindow.geometry("500x500")
    adPlayWindow.geometry("500x200")
    
    ## Function to find Existing Playlists
    def playlistExists():
        db = connect_to_database()
        cursor = db.cursor()
        val = enterPlaylistName.get()
        query1 = f"SELECT EXISTS (SELECT playlistTitle FROM playlists WHERE playlistTitle = \"{val}\")"
        cursor.execute(query1)
        result = cursor.fetchall()
        cursor.close()
        if result == [(0,)]:
            SearchLabel.config(text = "Available Title")
            addButton.pack()
            deleteButton.pack_forget()
        else:
            SearchLabel.config(text = "Taken Title")
            deleteButton.pack()
            addButton.pack_forget()
    
    # Function to add playlists, need to complete
    def addPlaylist():
        db = connect_to_database()
        cursor = db.cursor()
        query1 = f"SELECT * FROM Playlists"
        cursor.execute(query1)
        result1 = cursor.fetchall()
        print(result1)
        
        val = enterPlaylistName.get()
        query = f"INSERT INTO Playlists (playlistTitle) VALUES (\'{val}\')"
        cursor.execute(query)
        
        cursor.execute(query1)
        result2 = cursor.fetchall()
        db.commit()
        cursor.close()
        print(result2)
    
    # Function to delete playlists
    def deletePlaylist():
        db = connect_to_database()
        cursor = db.cursor()
        
        query1 = f"SELECT * FROM Playlists"
        cursor.execute(query1)
        result1 = cursor.fetchall()
        print(result1)
        
        val = enterPlaylistName.get()
        query = f"DELETE FROM Playlists WHERE playlistTitle = \"{val}\""
        cursor.execute(query)
        
        cursor.execute(query1)
        result2 = cursor.fetchall()
        print(result2)
        db.commit()
        cursor.close()
    
    ### Playlist Creation Popup Window ###
    ## Creating Name Entry ##
    NameFrame = Frame(adPlayWindow, highlightbackground = mainColor, highlightthickness = 5, highlightcolor= mainColor, bd = 0, bg = mainColor)
    NameFrame.place(relx = 0, rely = 0.01)
    PlaylistNameEntry = Entry(NameFrame,
                              textvariable= enterPlaylistName,
                              font = "Arial 20",
                              fg = acctColor,
                              bg = bkgndColor)
    PlaylistNameEntry.pack(side = RIGHT)
    PlaylistNameDirection = Label(NameFrame,
                                  text = 'Enter Playlist Name:',
                                  font = "Arial 15", 
                                  fg = acctColor,
                                  bg = bkgndColor,
                                  height = 2,
                                  width = 20)
    PlaylistNameDirection.pack(side = LEFT)
    
    ## Creating Checker
    SearchButtonFrame = Frame(adPlayWindow, highlightbackground = mainColor, highlightthickness= 5, bg = mainColor, bd= 0)
    SearchButtonFrame.place(relx = 0, rely = 0.30)
    SearchButton = Button(SearchButtonFrame, 
                          text = 'Check Playlist', 
                          font = 'Arial 15',
                          fg = acctColor,
                          bg = bkgndColor,
                          height = 2,
                          width = 21, 
                          command= playlistExists)
    SearchButton.pack(side = LEFT)
    SearchLabel = Label(SearchButtonFrame, 
                        text = 'Results Will Appear Soon',
                        font = "Arial 15",
                        fg = acctColor,
                        bg = bkgndColor,
                        height =  2,
                        width = 21)
    SearchLabel.pack(side = RIGHT)
    
    addDeleteFrame = Frame(adPlayWindow, highlightbackground= mainColor, highlightthickness= 5, bg = mainColor, bd = 0)
    addDeleteFrame.place(relx = 0, rely = 0.65)
    addButton = Button(addDeleteFrame, 
                       text="Add Playlist",
                       font = "Arial 15",
                       fg = acctColor,
                       bg = bkgndColor,
                       height=2,
                       width= 42,
                       command= addPlaylist)
    
    deleteButton = Button(addDeleteFrame,
                          text= "Delete Playlist",
                          font = 'Arial 15',
                          fg = acctColor,
                          bg = bkgndColor,
                          height= 2,
                          width= 42,
                          command = deletePlaylist)

## EDIT PLAYLIST POP UP WINDOW
def openEditPlayWindow():
    editPlayWindow = Toplevel(root)
    editPlayWindow.configure(bg = mainColor)
    editPlayWindow.title("Edit Playlists")
    editPlayWindow.geometry("500x350")
    
    db = connect_to_database()
    cursor = db.cursor()
        
    query1 = f"SELECT playlistTitle FROM Playlists"
    cursor.execute(query1)
    result1 = cursor.fetchall()
        
    query2 = f"SELECT songTitle FROM Songs"
    cursor.execute(query2)
    result2 = cursor.fetchall()
    
    # List to have all playlists
    playlistDisplayFrame = Frame(editPlayWindow, highlightbackground= mainColor, highlightthickness= 5, bg = mainColor, bd = 0)
    playlistDisplayFrame.place(relx = 0, rely = 0)
    ## NEEDS TO BE A RADIOBOX
    playlistDisplay = Listbox(playlistDisplayFrame,
                          exportselection= False,
                          font = "Arial 15",
                          fg = acctColor,
                          bg = bkgndColor,
                          highlightcolor = mainColor,
                          width= 21,
                          height= 10)
    for playlists in result1:
        playlistName = playlists[0]
        playlistDisplay.insert(END, f"{playlistName}")
    playlistDisplay.pack(side = LEFT, anchor= 'nw', padx=10)
    
    # List to have all songs
    songDisplay = Listbox(playlistDisplayFrame,
                          exportselection= False,
                          selectmode = "multiple",
                          font = "Arial 15",
                          fg = acctColor,
                          bg = bkgndColor,
                          highlightcolor = mainColor,
                          width= 21,
                          height= 10)
    for songs in result2:
        songName = songs[0]
        songDisplay.insert(END, f"{songName}")
    songDisplay.pack(side = RIGHT, anchor = 'ne')
    
    ## Select Playlist Function
    def selectAll():
        db = connect_to_database()
        cursor = db.cursor()
        
        selected = playlistDisplay.curselection()
        val = playlistDisplay.get(selected)
        query3 = f"SELECT playlistID FROM Playlists WHERE playlistTitle = \"{val}\""
        cursor.execute(query3)
        result1 = cursor.fetchall()
        
        for playlist in result1:
            playlistName = playlist[0]
        
        selected = songDisplay.curselection()
        selectedItems = []
        selectedIds = []
        
        for index in selected:
            selectedItems.append(songDisplay.get(index))
            query4 = f"SELECT songID FROM Songs WHERE songTitle = \"{songDisplay.get(index)}\""
            cursor.execute(query4)
            result2 = cursor.fetchone()
            processedIDs = result2[0]
            selectedIds.append(processedIDs)
            query5 = f"INSERT INTO PlaylistSongs (playlistID, songID) Values ({playlistName}, {processedIDs})"
            cursor.execute(query5)
            
        db.commit()
        cursor.close()
              
    songDisplayFrame = Frame(editPlayWindow, highlightbackground= mainColor, highlightthickness= 5, bg = mainColor, bd = 0)
    songDisplayFrame.place(relx= 0.05, rely = 0.75)
 
    # Want to be able to select a playlist, then select multiple songs to add.
    selectCurrentPlaylistButton = Button(songDisplayFrame,
                                         text = "Confirm Change",
                                         font = 'Arial 15',
                                         fg = acctColor,
                                         bg = bkgndColor,
                                         highlightcolor= mainColor,
                                         width = 15,
                                         height = 2,
                                         command = selectAll)
    selectCurrentPlaylistButton.pack(side = LEFT)
    
### Add / Delete Playlist ###
adPlayButtonBorder = Frame(playlistPage, highlightbackground = mainColor, highlightthickness = 5, bd = 0)
adPlayButtonBorder.place(relx = 0.2, rely = 0)
adPlayButton = Button(adPlayButtonBorder,
                      text = "Add/Delete Playlist",
                      font = "Arial 15",
                      fg = acctColor,
                      bg = bkgndColor,
                      width = 15,
                      height = 2,
                      command= openAdPlayWindow)
adPlayButton.pack()

### Edit Playlist ###
editPlayButtonBorder = Frame(playlistPage, highlightbackground = mainColor, highlightthickness = 5, bd = 0 )
editPlayButtonBorder.place(relx = 0.4, rely = 0)
editPlayButton = Button(editPlayButtonBorder,
                        text = "Edit Playlist",
                        font = "Arial 15",
                        fg = acctColor,
                        bg = bkgndColor,
                        width= 15,
                        height= 2,
                        command= openEditPlayWindow)
editPlayButton.pack()

### LIST BOX ###
### Creating List Boxes for Playlist Page ###
## Playlist ##
playlistLBBorder = Frame(playlistPage, highlightbackground = mainColor, highlightcolor=mainColor, bg = mainColor, highlightthickness= 5, bd = 0)
playlistLBBorder.place(relx = 0, rely = 0.2)
playlistListBox = Listbox(playlistLBBorder,
                          font = "Arial 15",
                          fg = acctColor,
                          bg = bkgndColor,
                          highlightcolor = mainColor,
                          width= 40,
                          height= 10)

## Song ##
songLBBorder = Frame(playlistPage, highlightbackground= mainColor, highlightcolor= mainColor, bg = mainColor, highlightthickness= 5, bd= 0)
songLBBorder.place(relx=1, rely = 0.2, anchor= 'ne')
songListBox = Listbox(songLBBorder,
                      font = "Arial 15",
                      fg= acctColor,
                      bg= bkgndColor,
                      highlightcolor= mainColor,
                      width=40,
                      height=10)

### Find playlist search results ###
def playlistLookupDB():
    db = connect_to_database()
    cursor = db.cursor()
    val = searchTextPlay.get()
    query1 = f"SELECT playlistTitle FROM Playlists WHERE playlistTitle LIKE \"%{val}%\""
    cursor.execute(query1)
    result = cursor.fetchall()
    cursor.close()
    playlistListBox.delete(0, END)
    for names in result:
        playlistName = names[0]
        playlistListBox.insert(END, f"{playlistName}")
    playlistListBox.pack()

def getPlaylistSelection():
    db = connect_to_database()
    cursor = db.cursor()
    selected = playlistListBox.curselection()
    #print(playlistListBox.get(selected))
    val = playlistListBox.get(selected)
    query1 = f"SELECT songTitle FROM Playlists NATURAL JOIN PlaylistSongs NATURAL JOIN Songs WHERE playlistTitle = \"{val}\""
    cursor.execute(query1)
    result = cursor.fetchall()
    cursor.close()
    songListBox.delete(0, END)
    for songs in result:
        songName = songs[0]
        songListBox.insert(END, f"{songName}")
    songListBox.pack()
    
### Find song search results in a playlist ###
def songLookupDB():   
    db = connect_to_database()
    cursor = db.cursor()
    val = searchTextSong.get()
    query = f"SELECT songTitle FROM Songs NATURAL JOIN PlaylistSongs NATURAL JOIN Playlists WHERE songTitle LIKE \"%{val}%\" "
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    songListBox.delete(0, END)
    for songs in result:
        songName = songs[0]
        songListBox.insert(END, f"{songName}")
    songListBox.pack()   

## Playlist Select button ##
selectPlaylistButtonBorder = Frame(playlistPage, highlightbackground= mainColor, highlightcolor= mainColor, bg = mainColor, highlightthickness= 5, bd= 0)
selectPlaylistButtonBorder.place(relx = 0, rely = 0.6)
selectPlaylistButton = Button(selectPlaylistButtonBorder,
                              text = "Select Playlist",
                              font = "Arial 15",
                              fg = acctColor,
                              bg = bkgndColor,
                              width=15,
                              height = 2,
                              command=getPlaylistSelection)
selectPlaylistButton.pack()

### Creating Playlist Search Bar ###
searchBorder = Frame(playlistPage, highlightbackground = mainColor, highlightcolor=mainColor, bg = mainColor, highlightthickness = 5, bd = 0)
searchBorder.place(relx = 0, rely = 0.1)
searchButton = Button(searchBorder, 
                     text = "Search Playlists: ",
                     font = "Arial 15",
                     fg = acctColor,
                     bg = bkgndColor,
                     width= 15,
                     height = 2,
                     command = playlistLookupDB)
searchButton.pack(side = LEFT)

searchEntry = Entry(searchBorder,
                    textvariable= searchTextPlay,
                    font = "Arial 20",
                    fg = acctColor,
                    bg = bkgndColor)
searchEntry.pack(side = RIGHT)

### Creating Song Search Bar ###
searchSongBorder = Frame(playlistPage, highlightbackground = mainColor, highlightcolor=mainColor, bg = mainColor, highlightthickness = 5, bd = 0)
searchSongBorder.place(relx = 1, rely = 0.1, anchor = 'ne')
searchSongButton = Button(searchSongBorder, 
                     text = "Search Songs: ",
                     font = "Arial 15",
                     fg = acctColor,
                     bg = bkgndColor,
                     width= 15,
                     height = 2,
                     command= songLookupDB)
searchSongButton.pack(side = LEFT)

searchSongEntry = Entry(searchSongBorder,
                    textvariable= searchTextSong,
                    font = "Arial 20",
                    fg = acctColor,
                    bg = bkgndColor)
searchSongEntry.pack(side = RIGHT)

### Song Management Page ###
# Connect to database
db = connect_to_database()
cursor = db.cursor()

# Query for getting all artists
artistQuery = f"SELECT artistTitle, label FROM Artists"
cursor.execute(artistQuery)
artistResult = cursor.fetchall()

# Query for getting all albums
albumQuery = f"SELECT albumTitle, artistTitle, genre, initialRelease FROM Albums"
cursor.execute(albumQuery)
albumResult = cursor.fetchall()

# Query for getting all Songs
songQuery = f"SELECT songTitle, albumTitle FROM Songs"
cursor.execute(songQuery)
songResult = cursor.fetchall()

# Query for getting all Special Releases
releaseQuery = f"SELECT albumTitle, altYear, remastered FROM Releases NATURAL JOIN albums"
cursor.execute(releaseQuery)
releaseResult = cursor.fetchall()

# Frame to hold listboxes 
listboxDisplayFrames = Frame(songPage, highlightbackground= mainColor, highlightthickness= 5, bg = mainColor, bd = 0)
listboxDisplayFrames.place(relx = 0.005, rely = 0.07)

# Label for Artsts
artistLabel = Label(listboxDisplayFrames,
                    text = "Artist Information",
                    font = 'Arial 15',
                    bg = bkgndColor,
                    fg= acctColor,
                    width= 44)
#artistLabel.pack(side = TOP, anchor = 'nw')
artistLabel.grid(row = 1, column= 0)

## Listbox to display artists and info
artistDisplay = Listbox(listboxDisplayFrames,
                        font = 'Arial 15',
                        fg = acctColor,
                        bg = bkgndColor,
                        highlightcolor= mainColor,
                        width = 44,
                        height = 7)
for artists in artistResult:
    artistName = artists[0]
    labelName = artists[1]
    artistDisplay.insert(END, f"{artistName}, Label: {labelName}")
#artistDisplay.pack(side = BOTTOM, anchor = 'sw')
artistDisplay.grid(row = 2, column=0)

# Label for Albums
albumLabel = Label(listboxDisplayFrames,
                   text = "Album Information",
                   font = 'Arial 15',
                   bg = bkgndColor,
                   fg = acctColor,
                   width= 44)
#albumLabel.pack(side = TOP, anchor= 'ne')
albumLabel.grid(row= 1, column=1)

## Listbox to display albums and info
albumDisplay = Listbox(listboxDisplayFrames,
                        font = 'Arial 15',
                        fg = acctColor,
                        bg = bkgndColor,
                        highlightcolor= mainColor,
                        width = 44,
                        height = 7)
for albums in albumResult:
    albumName = albums[0]
    artistName = albums[1]
    genre = albums[2]
    year = albums[3]
    albumDisplay.insert(END, f"{albumName}: {artistName}, {genre}, {year}")
#albumDisplay.pack(side = BOTTOM, anchor = 'se')
albumDisplay.grid(row = 2, column = 1)

# Label for Songs
songsLabel = Label(listboxDisplayFrames,
                   text = "Song Information",
                   font = 'Arial 15',
                   bg = bkgndColor,
                   fg = acctColor,
                   width= 44)
songsLabel.grid(row=3, column = 0)

## Listbox to display songs and info
songDisplay = Listbox(listboxDisplayFrames,
                        font = 'Arial 15',
                        fg = acctColor,
                        bg = bkgndColor,
                        highlightcolor= mainColor,
                        width = 44,
                        height = 7)
for songs in songResult:
    songName = songs[0]
    albumName = songs[1]
    songDisplay.insert(END, f"{songName}, {albumName}")
songDisplay.grid(row = 4, column = 0)

#Label for Releases
releaseLabel = Label(listboxDisplayFrames,
                   text = "Special Release Albums: Year, Remastered",
                   font = 'Arial 15',
                   bg = bkgndColor,
                   fg = acctColor,
                   width= 44)
releaseLabel.grid(row=3, column = 1)

## Listbox to Display Special Release info
releaseDisplay = Listbox(listboxDisplayFrames,
                        font = 'Arial 15',
                        fg = acctColor,
                        bg = bkgndColor,
                        highlightcolor= mainColor,
                        width = 44,
                        height = 7)
for versions in releaseResult:
    albumName = versions[0]
    year = versions[1]
    remastered = versions[2]
    releaseDisplay.insert(END, f"{albumName}: {year}, {remastered}")
releaseDisplay.grid(row = 4, column = 1)
cursor.close()


## Add/Delete Artist
# Pop Up window
def openArtistEditWin():
    artistEditWindow = Toplevel(root)
    artistEditWindow.configure(bg = mainColor)
    artistEditWindow.title("Add / Delete Artists")
    artistEditWindow.geometry("500x500")

    # Textbox and button to Search
    searchArtistBorder = Frame(artistEditWindow, highlightbackground = mainColor, highlightcolor=mainColor, bg = mainColor, highlightthickness = 5, bd = 0)
    searchArtistBorder.place(relx = 0, rely = 0)
    searchArtistButton = Button(searchArtistBorder, 
                     text = "Search Albums:",
                     font = "Arial 15",
                     fg = acctColor,
                     bg = bkgndColor,
                     width= 15,
                     height = 2)
    searchArtistButton.pack(side = LEFT)

    searchArtistEntry = Entry(searchArtistBorder,
                    textvariable= searchArtist,
                    font = "Arial 20",
                    fg = acctColor,
                    bg = bkgndColor)
    searchArtistEntry.pack(side = RIGHT)
    # Delete if Exists
    # Add Info

## Button to add/delete Artist
editArtistButton = Button(listboxDisplayFrames,
                          text = "Edit Artists",
                          font = 'Arial 15',
                          fg = acctColor,
                          bg = bkgndColor,
                          width= 22,
                          height= 2,
                          command= openArtistEditWin)

editArtistButton.grid(row = 5, column= 0, sticky = 'w')

## Add/Delete Album
# Pop Up Window
def openAlbumEditWin():
    albumEditWindow = Toplevel(root)
    albumEditWindow.configure(bg = mainColor)
    albumEditWindow.title("Add / Delete Albums")
    albumEditWindow.geometry("500x500")
    
    # Textbox to Search
    searchAlbumBorder = Frame(albumEditWindow, highlightbackground = mainColor, highlightcolor=mainColor, bg = mainColor, highlightthickness = 5, bd = 0)
    searchAlbumBorder.place(relx = 0, rely = 0)
    searchAlbumButton = Button(searchAlbumBorder, 
                     text = "Search Artists:",
                     font = "Arial 15",
                     fg = acctColor,
                     bg = bkgndColor,
                     width= 15,
                     height = 2)
    searchAlbumButton.pack(side = LEFT)

    searchAlbumEntry = Entry(searchAlbumBorder,
                    textvariable= searchAlbum,
                    font = "Arial 20",
                    fg = acctColor,
                    bg = bkgndColor)
    searchAlbumEntry.pack(side = RIGHT)
    # Delete if Exists
    # Search Artist
    # Add info 

# Button to add/delete album
editAlbumButton = Button(listboxDisplayFrames,
                          text = "Edit Albums",
                          font = 'Arial 15',
                          fg = acctColor,
                          bg = bkgndColor,
                          width= 22,
                          height= 2, 
                          command= openAlbumEditWin)

editAlbumButton.grid(row = 5, column= 0, sticky = 'e')

## Add/Delete Song
# Pop Up Window
def openSongEditWin():
    songEditWindow = Toplevel(root)
    songEditWindow.configure(bg = mainColor)
    songEditWindow.title("Add / Delete Songs")
    songEditWindow.geometry("500x500")
    
    # Textbox to Search
    searchSongBorder = Frame(songEditWindow, highlightbackground = mainColor, highlightcolor=mainColor, bg = mainColor, highlightthickness = 5, bd = 0)
    searchSongBorder.place(relx = 0, rely = 0)
    searchSongButton = Button(searchSongBorder, 
                     text = "Search Songs:",
                     font = "Arial 15",
                     fg = acctColor,
                     bg = bkgndColor,
                     width= 15,
                     height = 2)
    searchSongButton.pack(side = LEFT)

    searchSongEntry = Entry(searchSongBorder,
                    textvariable= searchSong,
                    font = "Arial 20",
                    fg = acctColor,
                    bg = bkgndColor)
    searchSongEntry.pack(side = RIGHT)
    # Delete If Exists
    # Search Album
    # Add info

# Button to add delete song
editSongButton = Button(listboxDisplayFrames,
                          text = "Edit Songs",
                          font = 'Arial 15',
                          fg = acctColor,
                          bg = bkgndColor,
                          width= 22,
                          height= 2,
                          command= openSongEditWin)

editSongButton.grid(row = 5, column= 1, sticky= 'w')
 
 ## Add/Delete Release
# Pop Up Window
def openReleaseEditWin():
    releaseEditWindow = Toplevel(root)
    releaseEditWindow.configure(bg = mainColor)
    releaseEditWindow.title("Add / Delete Releases")
    releaseEditWindow.geometry("500x500")
    # Textbox to Search
    # Delete If Exists
    # Search Album
    # Add info

# Button to add delete release   
editReleaseButton = Button(listboxDisplayFrames,
                          text = "Edit Release",
                          font = 'Arial 15',
                          fg = acctColor,
                          bg = bkgndColor,
                          width= 22,
                          height= 2, 
                          command = openReleaseEditWin)

editReleaseButton.grid(row = 5, column= 1, sticky= 'e')










# execute tkinter
root.mainloop()


### References ###
#1 Geeks for Geeks - Create First GUI Application using Python - Tkinter
# https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/#

#2 TutorialsPoint - How to center a label in a frame of fixed size in Tkinter?
# https://www.tutorialspoint.com/how-to-center-a-label-in-a-frame-of-fixed-size-in-tkinter

#3 TutorialsPoint - How to switch between two frames in Tkinter?
# https://www.tutorialspoint.com/how-to-switch-between-two-frames-in-tkinter

#4 Geeks for Geeks - Open a new window with a button in python - tkinter
# https://www.geeksforgeeks.org/open-a-new-window-with-a-button-in-python-tkinter/

#5 Geeks for Geeks - Python GUI - Tkinter
# https://www.geeksforgeeks.org/python-gui-tkinter/

#6 Home and Learn Python - Python: Database Connection 
# https://www.homeandlearn.uk/python-database-connect.html

#7 Tkinter Module and Tuples in Python 
# https://medium.com/@saifulj1234/tkinter-module-and-tuples-in-python-21aaebb9b7b0#:~:text=The%20third%20data%20type%20in,be%20at%20position%20one%2C%20etc.

#8 MariaDB Corporation - The Cursor Class
# https://mariadb-corporation.github.io/mariadb-connector-python/cursor.html

#9 MariaDB - ROW Syntax
# https://mariadb.com/kb/en/row/

#10 W3Schools SQL LIKE Operator
# https://www.w3schools.com/sql/sql_like.asp

#11 C# Corner - How to get items from a database into a Tkinter Listbox?
# https://www.c-sharpcorner.com/article/how-to-get-items-from-a-database-into-a-tkinter-listbox/

#12 Tutorials Point - Best Way to Test if a Row Exists in a MySQL Table
# https://www.tutorialspoint.com/best-way-to-test-if-a-row-exists-in-a-mysql-table#:~:text=To%20test%20whether%20a%20row,false%20is%20represented%20as%200.

#13 Medium - Python Tkinter Multi-Select Listboxes
# https://medium.com/@rushi.hacktivity/python-tinker-multiselect-listbox-e007ecd313d4

#14 Tutorials Point - How to Select at the Same Time from Two Tkinter Listboxes
# https://www.tutorialspoint.com/how-to-select-at-the-same-time-from-two-tkinter-listbox

#15 Stack Overflow - Tkinter Configure Column Widths
# https://stackoverflow.com/questions/14045271/tkinter-configure-columnwidth
