from mpd import MPDClient
from pathlib import Path

class MpdManager:
    def __init__(self, data):
        super().__init__()

        self.nowplaying = ''
        
        self.client = MPDClient()
        self.client.timeout = 10
        self.client.connect(data['host'], data['port'])
        print("Connected to mpd v: " + self.client.mpd_version) #TODO comment

    def status(self):
        return self.client.status()

    def stats(self):
        return self.client.stats()

    def playAlbum(self, album, playSong):
        self.client.stop()
        self.client.clear()
        #print(album[0]['path'].replace('\\', '/'))
        for song in album:
            self.client.add(song['path'].replace('\\', '/'))
        #self.client.add('AURI/Auri/01. The Space Between.flac')
        #self.client.add('F:\\Musicas\\Albuns\\AURI\\Auri\\01. The Space Between.flac')
        self.client.play(playSong)

    def getCoverArt(self):
        print('pegando a capa de: ' + self.nowplaying)
        print(self.client.albumart(self.nowplaying))

#TODO only change song if same album
#TODO order