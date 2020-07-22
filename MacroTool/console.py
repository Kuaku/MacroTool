import time
import threading

class consoleThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self);
        self.name = name
        self.threadID = threadID
        self.stop = False
        self.commands = {}
        self.commandsHelp = {}

    def stopThread(self):
        self.stop = True

    def addCommand(self, command, trigger, help):
        self.commands[command] = trigger;
        self.commandsHelp[command] = help

    def getCommands(self):
        return self.commandsHelp;

    def run(self):
        while not self.stop:
            inputCommand = input()
            if inputCommand in self.commands:
                self.commands[inputCommand]()
            else:
                print('--------command not found--------')
