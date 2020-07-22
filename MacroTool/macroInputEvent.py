import inputEvent
from pynput.keyboard import Controller, Key

class macroInputEvent (inputEvent.inputEvent):
    def __init__(self, activationString, macroList):
        super().__init__()
        self.disable(True)
        self.activationString = activationString
        self.macroList = macroList
        self.activationCount = 0
        self.activated = False
        self.macroCount = 0
        self.keyboard = Controller();

    def setConfigs(self, activationString, macroList):
        self.activationString = activationString
        self.macroList = macroList
        self.activationCount = 0
        self.activated = False
        self.macroCount = 0


    def setActivation(self, activation):
        self.activation = activation
        self.disable(False)

    def macroActivatedEvent(self, macro):
        self.activated = False
        self.macroCount = 0
        self.disable(True)
        for i in range(len(self.activationString)+len(macro['key'])):
            self.keyboard.press(Key.backspace)
            self.keyboard.release(Key.backspace)
        self.keyboard.type(macro['macro'])
        self.disable(False)

    def checkSpecialChar(self, key):
        try:
            inputChar = key.char
            return False
        except Exception as e:
            return True

    def trigger(self, key):
        isSpecial = self.checkSpecialChar(key)
        if not isSpecial and not self.activated:
            if key.char == self.activationString[self.activationCount]:
                self.activationCount += 1;
                if self.activationCount == len(self.activationString):
                    self.activated = True
                    self.activationCount = 0
            else:
                self.activationCount = 0
        elif not isSpecial:
            if self.macroCount == 0:
                possibles = []
                for i in range(len(self.macroList)):
                    if key.char == self.macroList[i]['key'][0]:
                        possibles.append(self.macroList[i]);
                self.activation.setPossibles(possibles);
            else:
                possibles = self.activation.getPossibles();
                for i in reversed(range(len(possibles))):
                    if len(possibles[i]['key']) <= self.macroCount:
                        del possibles[i]
                    elif not key.char == possibles[i]['key'][self.macroCount]:
                        del possibles[i]
                self.activation.setPossibles(possibles);
            self.macroCount += 1
            if len(self.activation.getPossibles()) == 0:
                self.activated = False
                self.macroCount = 0
