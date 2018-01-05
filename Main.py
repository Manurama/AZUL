from Sack import sack
from Scheibe import scheibe
from Zeile_in_Treppe import zeile_in_treppe
from Mittelscheibe import mittelscheibe
from Spielstein import spielstein
from Spielertableau import spielertableau
sack1 = sack()
scheibe1 = scheibe(sack1)
scheibe2 = scheibe(sack1)
mittelscheibe1 = mittelscheibe()
for i in scheibe1.steine_auf_scheibe:
    print(i.farbe)
print('*')
for i in scheibe2.steine_auf_scheibe:
    print(i.farbe)
scheibe1.steine_runternehmen(1, mittelscheibe1)
print('x')
for i in mittelscheibe1.steine_auf_scheibe:
    print(i.farbe)
scheibe2.steine_runternehmen(3, mittelscheibe1)
print('*')
for i in mittelscheibe1.steine_auf_scheibe:
    print(i.farbe)
strafliste = []
zeile1 = zeile_in_treppe(2)
steine = 5 * [spielstein(1)]
zeile1.steine_in_treppe(steine, strafliste)
print(zeile1.steinliste)
print(strafliste)
zeile1.steine_verlegen()
print(zeile1.fliessenfeld)
print(zeile1.steinliste)
print(zeile1.belegung)
spielertableau1 = spielertableau()
spielertableau1.belegungsmatrix = [[1, 1, 1, 1, 1], [0, 0, 1, 0, 0], [0, 1, 1, 0, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]
print(spielertableau1.zeilen[3].fliessenfeld)
print(spielertableau1.belegungsmatrix)
print(spielertableau1.punkte_bestimmen(0,2))