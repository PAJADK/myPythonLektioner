import re

class Materiale():

    def __init__(self, idnr=0, titel="", antal=0, antaludlaan=0, aarstal=9999):
        self.idnr = idnr
        self.titel = titel
        self.antal = antal
        self.antaludlaan = antaludlaan
        self.aarstal = aarstal

    def tostring(self):
        materiale = str(
            self.idnr) + ' - titelen: ' + self.titel + ' - antal kopier: ' + str(
            self.antal) + ' - udlånt: ' + str(
            self.antaludlaan) + ' - årstal: ' + str(self.aarstal)
        return materiale.title()

    def udlaan(self, antallaan):
        self.antaludlaan += antallaan
        return self.antaludlaan

    def kan_udlaane(self, antalkopi, antallaan):
        if antalkopi >= antallaan:
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

    def __init__(self, idnr=0, titel="", antal=0, antaludlaan=0, aarstal=9999, antalsider=0, forfatter=""):
        super().__init__(idnr, titel, antal, antaludlaan, aarstal)
        self.antalsider = antalsider
        self.forfatter = forfatter

    def tostring(self):
        bog = super().tostring() + ' - Antal sider: ' + str(self.antalsider) + ' - forfatter: ' + self.forfatter
        return bog.title()


class Film(Materiale):
    def __init__(self, idnr=0, titel="", antal=0, antaludlaan=0, aarstal=9999, instruktor="", lengde=0):
        super().__init__(idnr, titel, antal, antaludlaan, aarstal)
        self.instruktor = instruktor
        self.lengde = lengde

    def tostring(self):
        film = super().tostring() + ' - navnet på instruktøren: ' + self.instruktor + ' - antal minutter: ' + str(self.lengde)
        return film.title()
