#TODO optimze imports (?)
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Eliza')
        centralWidget = QWidget() #central widget
        self.layout = QVBoxLayout() #main layout, shared
        centralWidget.setLayout(self.layout)
        self.setCentralWidget(centralWidget)

        #initializing the ui
        self.bar = self.menuBar()
        self.createToolbar()
        self.createSearchbar()
        self.createGridList()
        self.createStatusbar()

    def createGridList(self):
        libraryLayout = QHBoxLayout()
        npLayout = QHBoxLayout()

        artistsLabel = QLabel("Artists")
        albumsLabel = QLabel("Albums")
        songsLabel = QLabel("Songs")
        queueLabel = QLabel("Queue")
        caLabel = QLabel("Now Playing")

        artistsLayout = QVBoxLayout()
        albumsLayout = QVBoxLayout()
        songsLayout = QVBoxLayout()
        queueLayout = QVBoxLayout()
        caLayout = QVBoxLayout()

        caLayout.setAlignment(Qt.AlignTop)

        artists = QListWidget()
        albums = QListWidget()
        songs = QListWidget()
        queueWidget = QListWidget()

        artistsLayout.addWidget(artistsLabel)
        artistsLayout.addWidget(artists)

        albumsLayout.addWidget(albumsLabel)
        albumsLayout.addWidget(albums)

        songsLayout.addWidget(songsLabel)
        songsLayout.addWidget(songs)

        queueLayout.addWidget(queueLabel)
        queueLayout.addWidget(queueWidget)

        coverart = QLabel(self)
        coverart.setPixmap(QPixmap("resources/artplaceholder.jpg"))
        coverart.setMaximumSize(300, 300)
        caLayout.addWidget(caLabel)
        caLayout.addWidget(coverart)
        npLayout.addLayout(caLayout)
        npLayout.addLayout(queueLayout)

        artists.addItem("All Artists")
        albums.addItem("All Albums")
        songs.addItem("1. Kuolevainen")
        
        libraryLayout.addLayout(artistsLayout)
        libraryLayout.addLayout(albumsLayout)
        libraryLayout.addLayout(songsLayout)

        self.layout.addLayout(libraryLayout)
        self.layout.addLayout(npLayout)

    def createToolbar(self):
        fileMenu = self.bar.addMenu('File')
        editMenu = self.bar.addMenu('Edit')
        helpMenu = self.bar.addMenu('Help')
        aboutMenu = self.bar.addMenu('About')

    def createSearchbar(self):
        searchbarLayout = QHBoxLayout()
        searchLine = QLineEdit()
        searchLine.setPlaceholderText('Artist, album or song')

        searchComboBox = QComboBox()
        searchComboBox.addItem("Artist");
        searchComboBox.addItem("Album");
        searchComboBox.addItem("Song");

        searchbarLayout.addWidget(searchLine)
        searchbarLayout.addWidget(searchComboBox)

        self.layout.addLayout(searchbarLayout)

    def createStatusbar(self):
        statusbar = QStatusBar()
        statusbar.showMessage('salve salve')
        self.layout.addWidget(statusbar)