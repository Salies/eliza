from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLabel, QPushButton, QSlider, QStatusBar
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
from eliza.libmanager import LibMng
from eliza.mpdclient import MpdClient

class MainWindow(QMainWindow):
    def __init__(self, libPath, mpdPath):
        super().__init__()

        self.__mng = LibMng(libPath, mpdPath)
        self.__mpd = MpdClient()

        #initializing all variables
        centralWidget = QWidget()
        self.__centralLayout = QVBoxLayout()
        self.__artistList = QListWidget()
        self.__albumList = QListWidget()
        self.__trackList = QListWidget()
        self.__queueList = QListWidget()
        self.__coverArt = QLabel()
        self.__songTime = QLabel("0:00/0:00")
        self.__playButton = QPushButton()
        self.__skipButton = QPushButton()
        self.__backButton = QPushButton()
        self.__shufButton = QPushButton()
        self.__reptButton = QPushButton()
        self.__seekBar = QSlider(Qt.Horizontal)
        self.__volBar = QSlider(Qt.Horizontal)
        self.__statusBar = QStatusBar()

        self.setWindowTitle('Eliza')
        centralWidget.setLayout(self.__centralLayout)
        self.setCentralWidget(centralWidget)
        self.__createGridList()
        self.__createNowPlaying()
        self.__createControlBar()

    def __createGridList(self):
        libraryLayout = QHBoxLayout()
        auxLayout = QVBoxLayout()

        auxLayout.addWidget(QLabel("Artists"))
        auxLayout.addWidget(self.__artistList)
        self.__artistList.addItem("All Artists")
        self.__artistList.insertItems(1, self.__mng.getArtists())
        self.__artistList.itemClicked.connect(self.__fillAlbums)

        libraryLayout.addLayout(auxLayout)

        auxLayout = None
        auxLayout = QVBoxLayout()

        auxLayout.addWidget(QLabel("Albums"))
        auxLayout.addWidget(self.__albumList)
        self.__albumList.itemClicked.connect(self.__fillTracks)

        libraryLayout.addLayout(auxLayout)

        auxLayout = None
        auxLayout = QVBoxLayout()

        auxLayout.addWidget(QLabel("Tracks"))
        auxLayout.addWidget(self.__trackList)
        self.__trackList.itemDoubleClicked.connect(self.__trackClicked)

        libraryLayout.addLayout(auxLayout)

        auxLayout = None

        self.__centralLayout.addLayout(libraryLayout)
        return
    
    def __createNowPlaying(self):
        layout = QHBoxLayout()
        auxLayout = QVBoxLayout()

        auxLayout.addWidget(QLabel("Now Playing"))

        self.__coverArt.setPixmap(QPixmap('qrc/img/artplaceholder.jpg'))
        self.__coverArt.setMaximumSize(300, 300)
        self.__coverArt.setScaledContents(True)
        
        auxLayout.addWidget(self.__coverArt)
        auxLayout.addStretch() #TODO remove?

        layout.addLayout(auxLayout)

        auxLayout = None
        auxLayout = QVBoxLayout()

        auxLayout.addWidget(QLabel("Queue"))
        auxLayout.addWidget(self.__queueList)

        layout.addLayout(auxLayout)

        auxLayout = None

        self.__centralLayout.addLayout(layout)
        return

    def __createControlBar(self):
        buttonSize = QSize(32, 32)
        playbarLayout = QHBoxLayout()
        seekLayout = QVBoxLayout()
        volumeLabel = QLabel()

        self.__playButton.setIconSize(buttonSize)
        self.__skipButton.setIconSize(buttonSize)
        self.__backButton.setIconSize(buttonSize)
        self.__shufButton.setIconSize(buttonSize)
        self.__reptButton.setIconSize(buttonSize)

        self.__playButton.setIcon(QIcon('qrc/btn/play.png'))
        self.__skipButton.setIcon(QIcon('qrc/btn/forward.png'))
        self.__backButton.setIcon(QIcon('qrc/btn/back.png'))
        self.__shufButton.setIcon(QIcon('qrc/btn/shuffle.png'))
        self.__reptButton.setIcon(QIcon('qrc/btn/repeat.png'))

        playbarLayout.addWidget(self.__backButton)
        playbarLayout.addWidget(self.__playButton)
        playbarLayout.addWidget(self.__skipButton)

        playbarLayout.addLayout(seekLayout)

        self.__volBar.setMaximumWidth(100)

        seekLayout.addWidget(self.__seekBar)
        seekLayout.addWidget(self.__songTime)

        volumeLabel.setPixmap(QPixmap('qrc/btn/volume.png'))

        playbarLayout.addWidget(volumeLabel)
        playbarLayout.addWidget(self.__volBar)

        self.__centralLayout.addLayout(playbarLayout)
        return

    #SLOTS
    def __fillAlbums(self, item):
        self.__mng.setAlbums(item.text(), self.__albumList)

    def __fillTracks(self, item):
        self.__mng.setTracks(item.data(Qt.UserRole), self.__trackList)

    def __trackClicked(self, item):
        tList = []
        for i in range(0, self.__trackList.count()):
            tList.append(self.__trackList.item(i).data(Qt.UserRole))
        self.__mpd.playAlbum(tList.index(item.data(Qt.UserRole)), tList)