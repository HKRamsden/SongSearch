###### Imports #####
from tkinter import * 
from tkinter import filedialog
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
    
def openEditPlayWindow():
    editPlayWindow = Toplevel(root)
    editPlayWindow.configure(bg = mainColor)
    editPlayWindow.title("Edit Playlists")
    editPlayWindow.geometry("500x500")
    
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

### Defining Variables for text input ###
searchTextPlay = StringVar()
searchTextSong = StringVar()

### Find playlist search results ###
def playlistLookupDB():
    db = connect_to_database()
    cursor = db.cursor()
    val = searchTextPlay.get()
    query1 = f"SELECT playlistTitle FROM Playlists WHERE playlistTitle LIKE \"%{val}%\""
    cursor.execute(query1)
    result = cursor.fetchall()
    cursor.close()
    for names in result:
        playlistName = names[0]
        playlistListBox.insert(END, f"{playlistName}")
    playlistListBox.pack()

def getPlaylistSelection():
    db = connect_to_database()
    cursor = db.cursor()
    selected = playlistListBox.curselection()
    print(playlistListBox.get(selected))
    val = playlistListBox.get(selected)
    query1 = f"SELECT songTitle FROM Playlists NATURAL JOIN PlaylistSongs NATURAL JOIN Songs WHERE playlistTitle = \"{val}\""
    cursor.execute(query1)
    result = cursor.fetchall()
    cursor.close()
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