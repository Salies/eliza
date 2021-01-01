from PyQt5.QtWidgets import QApplication
from eliza.mainwindow import MainWindow

app = QApplication([])

window = MainWindow()
window.show()
#window = MainWindow()
app.exec()