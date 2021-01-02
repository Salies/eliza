from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class ArtistList(QListWidget):
    def __init__(self):
        super().__init__()
        self.addItem('All Artists')
    
    def fill(self, data): #https://wiki.python.org/moin/PyQt/Adding%20items%20to%20a%20list%20widget
        for artist in data:
            item = QListWidgetItem("%s" % artist)
            self.addItem(item)

class AlbumList(QListWidget):
    def __init__(self):
        super().__init__()
    
    def fill(self, data):
        self.clear()
        for album in data:
            item = QListWidgetItem("%s" % album['album'])
            item.setData(Qt.UserRole, album['id'])
            self.addItem(item)

class TrackList(QListWidget):
    def __init__(self):
        super().__init__()
    
    def fill(self, data):
        self.clear()
        for track in data:
            item = QListWidgetItem("%s" % track['title'])
            self.addItem(item)