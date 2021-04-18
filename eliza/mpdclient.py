import musicpd

class MpdClient:
    def __init__(self):
        self.__client = musicpd.MPDClient() 
        self.__client.connect()
        self.__client.update()
        print(self.__client.mpd_version)
    
    def playAlbum(self, sel, list):
        self.__client.command_list_ok_begin()
        self.__client.clear()
        self.__client.stop()

        for item in list:
            self.__client.add(item)

        self.__client.play(sel)
        self.__client.command_list_end()

        return

    def __del__(self):
        self.__client.disconnect()