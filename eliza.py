import configparser
from PyQt5.QtWidgets import QApplication
from eliza.mainwindow import MainWindow

config = configparser.ConfigParser()
config.read('eliza.ini')

app = QApplication([])

w = MainWindow(config['main']['lib'], config['mpd']['music_directory'])

w.show()
app.exec()