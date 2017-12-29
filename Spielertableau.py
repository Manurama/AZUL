from Zeile_in_Treppe import zeile_in_treppe

class spielertableau:

    def __init__(self):
        self.spielstand = 0
        self.zeilen = [zeile_in_treppe(n) for n in range(1,6)]
        self.strafzeile = []
        self.belegungsmatrix = [z.belegung for z in self.zeilen]