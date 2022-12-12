VOITTAVAT_SIIRROT = {
    "k": "s",
    "s": "p",
    "p": "k",
}


# Luokka pitää kirjaa ensimmäisen ja toisen pelaajan pisteistä sekä tasapelien
# määrästä.
class Tuomari:
    def __init__(self):
        self.ekan_pisteet = 0
        self.tokan_pisteet = 0
        self.tasapelit = 0

    def kirjaa_siirto(self, ekan_siirto, tokan_siirto):
        if self._tasapeli(ekan_siirto, tokan_siirto):
            self.tasapelit = self.tasapelit + 1
        elif self._eka_voittaa(ekan_siirto, tokan_siirto):
            self.ekan_pisteet = self.ekan_pisteet + 1
        else:
            self.tokan_pisteet = self.tokan_pisteet + 1

    def ilmoita_tilanne(self):
        return (
            f"Pelitilanne: {self.ekan_pisteet} - {self.tokan_pisteet}"
            f"\nTasapelit: {self.tasapelit}"
        )

    # sisäinen metodi, jolla tarkastetaan tuliko tasapeli
    def _tasapeli(self, eka, toka):
        return eka == toka

    # sisäinen metodi joka tarkastaa voittaako eka pelaaja tokan
    def _eka_voittaa(self, eka, toka):
        return VOITTAVAT_SIIRROT[eka] == toka


default_tuomari = Tuomari()
