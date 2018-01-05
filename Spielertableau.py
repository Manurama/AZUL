from Zeile_in_Treppe import zeile_in_treppe


class spielertableau:
    def __init__(self):
        self.spielstand = 0
        self.zeilen = [zeile_in_treppe(n) for n in range(1, 6)]
        self.strafzeile = []
        self.belegungsmatrix = [z.belegung for z in self.zeilen]

    def punkte_bestimmen(self, x_origin, y_origin):
        punkte = 0
        y = y_origin  # spalte
        x = x_origin  # zeile

        # falls y nicht in der Spalte ganz links, y Wert bis zum ersten belegten platz schieben
        while True:
            if y > 0:
                if self.belegungsmatrix[x_origin][y - 1] == 1:
                    y -= 1
                else:
                    break
            else:
                break

        # falls y verschoben wurde oder der Platz weiter rechts belegt ist sollen alle zusammenhängenden belegten
        # Plätze nach rechts aufaddiert werden

        if y != y_origin or self.belegungsmatrix[x_origin][(y + 1) % 5] == 1:
            zeileSum = 0
            for i in range(y, 5):
                if self.belegungsmatrix[x_origin][i] == 1:
                    punkte += 1
                    zeileSum += 1
                    if zeileSum == 5:  # Extrapunkte für volle Zeile
                        punkte += 2
                else:
                    break

        while True:
            if x > 0:
                if self.belegungsmatrix[x - 1][y_origin] == 1:
                    x -= 1
                else:
                    break
            else:
                break

        if x != x_origin or self.belegungsmatrix[(x + 1) % 5][y_origin] == 1:
            spalteSum = 0
            for i in range(x, 5):
                if self.belegungsmatrix[i][y_origin] == 1:
                    punkte += 1
                    spalteSum += 1
                    if spalteSum == 5:  # Extrapunkte für volle Spalte
                        punkte += 7
                else:
                    break

        # falls nur ein einzeln liegender Stein verlegt wurde gibt es einen Punkt
        if punkte == 0:
            punkte += 1
        return punkte
