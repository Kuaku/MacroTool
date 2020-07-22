class inputEvent:
    def __init__(self):
        self.disabled = False

    def disable(self, disable):
        self.disabled = disable

    def isDisabled(self):
        return self.disabled

    def trigger(self, key):
        print("{0} released".format(key))
