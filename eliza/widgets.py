from PyQt5.QtWidgets import *

class ArtistList(QListWidget):
    def __init__(self):
        super().__init__()
        self.addItem('All Artists')
    
    def fill(self, data): #https://wiki.python.org/moin/PyQt/Adding%20items%20to%20a%20list%20widget
        for artist in data:
            item = QListWidgetItem("%s" % artist)
            self.addItem(item)