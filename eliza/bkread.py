from pathlib import Path
import sqlite3

#TODO: remove unecessary conversions, like in getartistalbums(?)

def formatData(data): #TODO: is this how private functions work?
    return list(map(dict, data))

class Booker:
    def __init__(self, bkdir):
        print("eae")
        conn = sqlite3.connect(Path(bkdir))
        conn.row_factory = sqlite3.Row
        self.c = conn.cursor()      

    def getArtists(self):
        self.c.execute('SELECT name FROM artists')
        data = self.c.fetchall()

        return list(map(list,  zip(*data)))[0]
    
    def getArtistAlbums(self, artist):
        a = (artist,)
        self.c.execute('SELECT * FROM albums WHERE albumartist=?', a)

        return formatData(self.c.fetchall())

    def getAlbumTracks(self, albumId):
        i = (albumId,)
        self.c.execute('SELECT * FROM tracks WHERE albumid=?', i)

        return formatData(self.c.fetchall())
