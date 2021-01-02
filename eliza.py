import configparser
#from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from eliza.mainwindow import MainWindow

app = QApplication([])

config = configparser.ConfigParser()
config.read('eliza.conf')

window = MainWindow(config['dir']['booker'])

window.show()
app.exec()