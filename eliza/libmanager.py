import sqlite3
from pathlib import Path
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtCore import Qt
from os import remove

class LibMng:
    def __init__(self, path, mpdPath):
        self.__mpdPath = mpdPath
        self.__con = sqlite3.connect(Path(path))
        self.__cur = self.__con.cursor()

    def getArtists(self):
        artists = []
        for row in self.__cur.execute('SELECT albumartist FROM albums'):
            if not row[0]:
                artists.append("(unnamed)")
                continue
            artists.append(row[0])
        return sorted(list(set(artists)))

    def setAlbums(self, artist, qList):
        qList.clear()
        item = None
        for row in self.__cur.execute('SELECT id, album FROM albums Where albumartist = "' + artist + '"'):
            n = row[1]
            if not row[1]:
                n = "(unnamed)"
            item = QListWidgetItem(n)
            item.setData(Qt.UserRole, row[0]) #hardcoded it so I don't have to import Qt
            qList.addItem(item)
            item = None
        return
    
    def setTracks(self, albumId, qList):
        qList.clear()
        item = None
        for row in self.__cur.execute("SELECT title, hex(path) FROM items Where album_id = " + str(albumId)):
            n = row[0]
            if not row[0]:
                n = "(unnamed)"
            item = QListWidgetItem(n)
            p = Path(bytes.fromhex(row[1]).decode('utf-8')).as_posix().replace(self.__mpdPath, '')
            if(p[0] == "/"):
                p = p.replace("/", "", 1)
            item.setData(Qt.UserRole, str(p))
            qList.addItem(item)
            item = None
        return

    def __del__(self):
        self.__con.close()
        #if(Path('cover.bin').is_file()):
        #    remove('cover.bin')