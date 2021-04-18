from threading import Timer, Thread

class ThreadTimer(Thread):
    def __init__(self, event, callback):
        Thread.__init__(self)
        self.stopped = event
        self.__callback = callback

    def run(self):
        while not self.stopped.wait(0.5):
            self.__callback()