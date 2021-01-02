import configparser
#from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from eliza.mainwindow import MainWindow

app = QApplication([])

config = configparser.ConfigParser()
config.read('eliza.conf') #TODO: ADD ERROR IF FILE DOESN'T EXIST

window = MainWindow([config['dir']['booker'], config['mpd']])

window.show()
app.exec()