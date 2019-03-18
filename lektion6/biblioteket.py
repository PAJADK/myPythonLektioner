import re

class Materiale():

    def __init__(self, idnr=0, titel="", antal=2, antaludlaan=2, aarstal=9999):
        self.idnr = idnr
        self.titel = titel
        self.antal = antal
        self.antaludlaan = antaludlaan
        self.aarstal = aarstal

    def tostring(self):
        materiale = str(
            self.idnr) + ' - Hvad er titelen: ' + self.titel + ' - Hvor mange kopier har biblioteket: ' + str(
            self.antal) + ' - Hvor mange er udlånt: ' + str(
            self.antaludlaan) + ' - Hvilket årstal er: ' + str(self.aarstal)
        return materiale.title()

    def udlaan(self, tjek_udlaan):
        self.antaludlaan += tjek_udlaan

    def kan_udlaane(self, tjek_antal):
        if tjek_antal <= self.antaludlaan:
            return True
        else:
            return False
"""
    def match_titel(self, search):
        if re.search(self.titel, re.IGNORECASE):
            return True
         else:
            return False
"""

class Bog(Materiale):

    def __init__(self, idnr=0, titel="", antal=3, antaludlaan=2, aarstal=9999, antalsider=0, forfatter=""):
        super().__init__(idnr, titel, antal, antaludlaan, aarstal)
        self.antalsider = antalsider
        self.forfatter = forfatter

    def tostring(self):
        bog = str(self.idnr) + ' - Hvad er titelen: ' + self.titel + ' - Hvor mange kopier har biblioteket: ' + str(
            self.antal) + ' - Hvor mange er udlånt: ' + str(
            self.antaludlaan) + ' - Hvilket årstal er: ' + str(
            self.aarstal) + ' - Antal sider: ' + str(self.antalsider) + ' - forfatterens navn: ' + self.forfatter
        return bog


class Film(Materiale):
    def __init__(self, idnr=0, titel="", antal=0, antaludlaan=0, aarstal=9999, instruktor="", lengde=0):
        super().__init__(idnr, titel, antal, antaludlaan, aarstal)
        self.instruktor = instruktor
        self.lengde = lengde

    def tostring(self):
        film = str(self.idnr) + ' - Hvad er titelen: ' + self.titel + ' - Hvor mange kopier har biblioteket: ' + str(
            self.antal) + ' - Hvor mange er udlånt: ' + str(
            self.antaludlaan) + ' - Hvilket årstal er: ' + str(
            self.aarstal) + ' - navnet på instruktøren: ' + self.instruktor + ' - antal minutter: ' + str(self.lengde)
        return film
