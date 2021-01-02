import configparser
#from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from eliza.mainwindow import MainWindow
from eliza.bkread import Booker

class Manager(QObject):
    def __init__(self, bkrdir):
        print('bkrdir: ' + bkrdir)
        self.booker = Booker(bkrdir)
    
    def initApp(self, mainwindow):
        self.mainwindow = mainwindow # recieves the window later on, starts operating with it

        print('iniciando as operacoes')
        self.mainwindow.artists.fill(self.booker.getArtists())

app = QApplication([])

config = configparser.ConfigParser()
config.read('eliza.conf')

manager = Manager(config['dir']['booker'])
window = MainWindow(manager)

manager.initApp(window)

window.show()
app.exec()