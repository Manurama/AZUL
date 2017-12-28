from Sack import sack
from Spielstein import spielstein

class scheibe:
    def __init__(self, sack):
        self.steine_auf_scheibe = []
        for i in range (4):
            self.steine_auf_scheibe.append(sack.stein_rausnehmen())

    def steine_runternehmen(self, farbe, mittelfeld):
        count = 0
        runtergenommene_steine = []
        restl_steine= []
        for i in self.steine_auf_scheibe:
            if i.farbe == farbe:
                runtergenommene_steine.append(i)
                count+=1
            else:
                restl_steine.append(i)
        if count == 0:
            return False
        else:
            mittelfeld.steine_auf_scheibe.extend(restl_steine)
            self.steine_auf_scheibe=[]
            return runtergenommene_steine




