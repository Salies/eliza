import configparser
#from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from eliza.mainwindow import MainWindow
from eliza.bkread import Booker

class Manager(QObject):
    def __init__(self, bkrdir):
        print()

#TODO: pass booker stuff to a manager class that deals with the ui(?)

app = QApplication([])
config = configparser.ConfigParser()
config.read('eliza.conf')

booker = Booker(config['dir']['booker'])

#print(booker.getArtists())

#print(booker.getArtistAlbums('Ok Goodnight'))

#print(booker.getAlbumTracks(75) )

window = MainWindow()

window.artists.fill(booker.getArtists())

window.show()
app.exec()