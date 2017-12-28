from Scheibe import scheibe

class mittelscheibe(scheibe):
    def __init__(self):
        self.steine_auf_scheibe = []

    def steine_runternehmen(self, farbe):
        count = 0
        runtergenommene_steine = []
        for i in self.steine_auf_scheibe():
            if i.farbe == farbe:
                runtergenommene_steine.append(i)
                count += 1
        if count == 0:
            return False
        else:
            return runtergenommene_steine
