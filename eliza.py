import configparser
from PyQt5.QtWidgets import QApplication, QMessageBox
from eliza.mainwindow import MainWindow

app = QApplication([])
config = configparser.ConfigParser()
config.read('eliza.conf')

print(config['dir']['booker'])

#loading config file
#try:
#    config.read('./eliza.conf')
#except configparser.MissingSectionHeaderError:
#    msg = QMessageBox()
#    msg.setIcon(QMessageBox.Critical)
#    msg.setText("Couldn't open config file")
#    msg.setInformativeText("eliza.conf couldn't be opened or isn't valid. Create it if doesn't exist.")
#    msg.setWindowTitle("Eliza")
#    msg.exec()
#    quit()
#finally:
#    print(config['DEFAULT'])

window = MainWindow()
window.show()
app.exec()