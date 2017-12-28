from Spielstein import spielstein
from random import shuffle

class sack:
    def __init__(self):
        self.sacklist = [spielstein(5)]*20+[spielstein(1)]*20+[spielstein(2)]*20+[spielstein(3)]*20+[spielstein(4)]*20
        shuffle(self.sacklist)

    def stein_rausnehmen(self):
        return self.sacklist.pop()

    def sack_leer(self):
        if self.sacklist:
            return True
        else:
            return False

