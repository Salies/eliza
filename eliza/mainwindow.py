#TODO optimze imports (?)
#TODO privatize functions (?)
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from eliza.widgets import *
from eliza.bkread import Booker
from eliza.mpdmanager import MpdManager

from os import path

class MainWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()

        #basic values
        self.setWindowTitle('Eliza')
        centralWidget = QWidget() #central widget
        self.layout = QVBoxLayout() #main layout, shared
        centralWidget.setLayout(self.layout)
        self.setCentralWidget(centralWidget)
        self.currentAlbum = []
        self.coverart = QLabel()

        #booker
        self.bkr = Booker(data[0])

        #mpd
        self.mpdmng = MpdManager(data[1])

        #initializing the ui
        self.bar = self.menuBar()
        self.initUi()

    def initUi(self):
        self.createToolbar()
        self.createSearchbar()
        self.createGridList()
        self.createPlaybar()
        self.createStatusbar()
        self.initSignals()
        self.setStates()

    def setStates(self):
        initStatus = self.mpdmng.status()
        #print(initStatus)

    def initSignals(self):
        self.artists.fill(self.bkr.getArtists())
        self.artists.itemClicked.connect(self.fillAlbums)
        self.albums.itemClicked.connect(self.fillTracks)
        self.songs.itemDoubleClicked.connect(self.playAlbum)

    def fillAlbums(self, item):
        self.albums.fill(self.bkr.getArtistAlbums(item.text()))

    def fillTracks(self, item):
        self.currentAlbum = self.bkr.getAlbumTracks(item.data(Qt.UserRole))
        self.songs.fill(self.currentAlbum)

    def playAlbum(self, item):
        print('ALBUM ATUAL: %d' % self.currentAlbum[item.data(Qt.UserRole)]['albumid'])
        self.mpdmng.playAlbum(self.currentAlbum, item.data(Qt.UserRole))
        artPath = path.join(self.bkr.datapath, 'coverarts', str(self.currentAlbum[item.data(Qt.UserRole)]['albumid'])) + '.jpg'
        print(artPath)
        self.coverart.setPixmap(QPixmap(artPath))

    def createGridList(self):
        libraryLayout = QHBoxLayout()
        npLayout = QHBoxLayout()

        artistsLabel = QLabel('Artists')
        albumsLabel = QLabel('Albums')
        songsLabel = QLabel('Songs')
        queueLabel = QLabel('Queue')
        caLabel = QLabel('Now Playing')

        artistsLayout = QVBoxLayout()
        albumsLayout = QVBoxLayout()
        songsLayout = QVBoxLayout()
        queueLayout = QVBoxLayout()
        caLayout = QVBoxLayout()

        caLayout.setAlignment(Qt.AlignTop)

        self.artists = ArtistList()
        self.albums = AlbumList()
        self.songs = TrackList()
        queueWidget = QListWidget()

        artistsLayout.addWidget(artistsLabel)
        artistsLayout.addWidget(self.artists)

        albumsLayout.addWidget(albumsLabel)
        albumsLayout.addWidget(self.albums)

        songsLayout.addWidget(songsLabel)
        songsLayout.addWidget(self.songs)

        queueLayout.addWidget(queueLabel)
        queueLayout.addWidget(queueWidget)

        self.coverart.setPixmap(QPixmap("resources/img/artplaceholder.jpg"))
        self.coverart.setMaximumSize(300, 300)
        self.coverart.setScaledContents(True)
        caLayout.addWidget(caLabel)
        caLayout.addWidget(self.coverart)
        npLayout.addLayout(caLayout)
        npLayout.addLayout(queueLayout)
        
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

    def createPlaybar(self):
        buttonSize = QSize(32, 32)
        icons = [['play', 'pause'], ['repeat', 'repeat_none', 'repeat_song'], ['shuffle'], 'forward', 'back']

        seekLayout = QVBoxLayout()

        playbarLayout = QHBoxLayout()
        playIcon = QIcon('resources/icon/' + icons[0][0] + '.png')
        playButton = QPushButton()
        playButton.setIcon(playIcon)
        playButton.setIconSize(buttonSize)

        backIcon = QIcon('resources/icon/' + icons[4] + '.png')
        backButton = QPushButton()
        backButton.setIcon(backIcon)
        backButton.setIconSize(buttonSize)

        forwardIcon = QIcon('resources/icon/' + icons[3] + '.png')
        forwardButton = QPushButton()
        forwardButton.setIcon(forwardIcon)
        forwardButton.setIconSize(buttonSize)

        seekbar = QSlider(Qt.Horizontal)
        seekLayout.addWidget(seekbar)

        songTime = QLabel('0:00/0:00')
        seekLayout.addWidget(songTime)

        shuffleIcon = QIcon('resources/icon/' + icons[2][0] + '.png')
        shuffleButton = QPushButton()
        shuffleButton.setIcon(shuffleIcon)
        shuffleButton.setIconSize(buttonSize)

        repeatIcon = QIcon('resources/icon/' + icons[1][0] + '.png')
        repeatButton = QPushButton()
        repeatButton.setIcon(repeatIcon)
        repeatButton.setIconSize(buttonSize)
        
        playbarLayout.addWidget(backButton)
        playbarLayout.addWidget(playButton)
        playbarLayout.addWidget(forwardButton)
        playbarLayout.addLayout(seekLayout)
        playbarLayout.addWidget(shuffleButton)
        playbarLayout.addWidget(repeatButton)

        volumeLabel = QLabel()
        volumeLabel.setPixmap(QPixmap('resources/img/volume.png'))

        self.volumebar = QSlider(Qt.Horizontal)
        self.volumebar.setMaximumWidth(100);

        playbarLayout.addWidget(volumeLabel)
        playbarLayout.addWidget(self.volumebar)

        self.layout.addLayout(playbarLayout)

    def createStatusbar(self):
        statusbar = QStatusBar()
        stats = self.mpdmng.stats()
        statusbar.showMessage('%s artists | %s albums | %s songs' % (stats['artists'], stats['albums'], stats['songs']))
        self.layout.addWidget(statusbar)
    
    #signals
    #@pyqtSlot(list)
    #def albumartistFetch(artist):
    #    print('CAPTEI A MENSAGEM:' + artist)
    #    pass