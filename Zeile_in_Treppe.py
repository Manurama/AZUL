
class zeile_in_treppe:
    def __init__(self, stufe):
        self.belegung = [0, 0, 0, 0, 0]
        self.stufe = stufe
        # Liste mit den Zahlen der Farbe welche im fließenfeld noch verlegtwerden kann

        self.fliessenfeld = [(x-self.stufe+1) % 5+1 for x in range(5)]
        self.farbe = 0
        self.ist_voll = False
        self.steinliste = []

    def steine_in_treppe(self, steine, strafliste):
        if not self.steinliste:
            self.farbe = steine[0].farbe
        if steine[0].farbe == self.farbe and not self.ist_voll:
                for i in steine:
                    if len(self.steinliste) < self.stufe:
                        self.steinliste.append(i)
                    else:
                        self.ist_voll = True
                        strafliste.append(i)
        else:
            return False
    
    # Steine von Liste in Fliessenfeld verlegen

    def steine_verlegen(self):
        if self.ist_voll:
            if int(self.farbe) in self.fliessenfeld:
                x = self.fliessenfeld.index(self.farbe)
                self.fliessenfeld[x] = self.steinliste[0]
                self.belegung[x] = 1
                self.steinliste = []