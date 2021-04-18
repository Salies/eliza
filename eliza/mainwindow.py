from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLabel, QPushButton, QSlider, QStatusBar
from PyQt5.QtCore import Qt
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
        self.__songTime = QLabel()
        self.__playButton = QPushButton()
        self.__skipButton = QPushButton()
        self.__backButton = QPushButton()
        self.__shufButton = QPushButton()
        self.__reptButton = QPushButton()
        self.__seekBar = QSlider()
        self.__volBar = QSlider()
        self.__statusBar = QStatusBar()

        self.setWindowTitle('Eliza')
        centralWidget.setLayout(self.__centralLayout)
        self.setCentralWidget(centralWidget)
        self.__createGridList()

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

    def __fillAlbums(self, item):
        self.__mng.setAlbums(item.text(), self.__albumList)

    def __fillTracks(self, item):
        self.__mng.setTracks(item.data(Qt.UserRole), self.__trackList)

    def __trackClicked(self, item):
        tList = []
        for i in range(0, self.__trackList.count()):
            tList.append(self.__trackList.item(i).data(Qt.UserRole))
        self.__mpd.playAlbum(tList.index(item.data(Qt.UserRole)), tList)