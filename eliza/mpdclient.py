import musicpd
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

class MpdClient:
    def __init__(self):
        self.__client = musicpd.MPDClient() 
        self.__client.connect()
        self.__client.update()
        print(self.__client.mpd_version)

    def stats(self):
        return self.__client.stats()

    def volume(self):
        return int(self.__client.status().get('volume'))

    def setVolume(self, val): #TODO: refazer as funções estilo essa
        self.__client.setvol(int(val))

    def pause(self):
        self.__client.pause()
    
    def playAlbum(self, sel, list, label):
        self.__client.command_list_ok_begin()
        self.__client.clear()
        self.__client.stop()

        for item in list:
            self.__client.add(item)

        self.__client.play(sel)
        self.__client.command_list_end()

        self.__loadCoverArt(list[0], label)

        return

    def justPlay(self, i):
        self.__client.play(i)

    def __loadCoverArt(self, track, label):
        art = self.__client.readpicture(track, 0)
        size = int(art['size'])
        done = int(art['binary'])
        with open('cover.bin', 'wb') as cover: #TODO: optimze album art loading // debug when embedded doesn't exist
            cover.write(art['data'])
            while size > done:
                art = self.__client.readpicture(track, done)
                done += int(art['binary'])
                cover.write(art['data'])

        pix = QPixmap('cover.bin')
        label.setPixmap(pix)

    def __del__(self):
        self.__client.disconnect()