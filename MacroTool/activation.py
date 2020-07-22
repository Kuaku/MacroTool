import time
import threading

class activationThread(threading.Thread):
    def __init__(self, threadID, name, trigger, threshhold):
        threading.Thread.__init__(self);
        self.name = name
        self.threadID = threadID
        self.lastPress = time.time()
        self.trigger = trigger
        self.stop = False
        self.possibles = []
        self.threshhold = threshhold


    def setThreshhold(self, threshhold):
        self.threshhold = threshhold


    def stopThread(self):
        self.stop = True

    def setPossibles(self, possibles):
        self.lastPress = time.time()
        self.possibles = possibles

    def getPossibles(self):
        return self.possibles

    def run(self):
        while not self.stop:
            if len(self.possibles) > 0:
                if time.time()-self.lastPress > self.threshhold:
                    self.trigger(self.possibles[0])
                    self.possibles = []
            time.sleep(0.01)
