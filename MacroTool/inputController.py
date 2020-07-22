from pynput.keyboard import Listener

class inputController:

    def __init__(self):
        self.controller = {}
        listener = Listener(
                on_release=self.on_release)
        listener.start();


    def on_release(self, key):
        for event in self.controller:
            if not self.controller[event].isDisabled():
                self.controller[event].trigger(key)

    def get(self, name):
        return self.controller[name]

    def addInputEvent(self, inputEvent, name):
        self.controller[name] = inputEvent
