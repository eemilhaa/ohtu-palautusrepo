from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = []

    def tavaroita_korissa(self):
        return sum([ostos.lukumaara() for ostos in self._ostokset])

    def hinta(self):
        return sum([ostos.hinta() for ostos in self._ostokset])

    def lisaa_tuote(self, lisattava: Tuote):
        ostoksen_lukumaara = self._muuta_ostoksen_lukumaaraa(lisattava, 1)
        if not ostoksen_lukumaara:
            self._lisaa_uusi_ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        ostoksen_lukumaara = self._muuta_ostoksen_lukumaaraa(poistettava, -1)
        if ostoksen_lukumaara < 1:
            self._poista_tyhjat_ostokset()

    def tyhjenna(self):
        self._ostokset = []

    def ostokset(self):
        return self._ostokset

    def _muuta_ostoksen_lukumaaraa(self, tuote: Tuote, muutos: int):
        for ostos in self._ostokset:
            if tuote.nimi() == ostos.tuotteen_nimi():
                ostos.muuta_lukumaaraa(muutos)
                return ostos.lukumaara()

    def _lisaa_uusi_ostos(self, lisattava: Tuote):
        ostos = Ostos(lisattava)
        self._ostokset.append(ostos)

    def _poista_tyhjat_ostokset(self):
        ostokset = filter(
            lambda ostos: ostos.lukumaara() > 0, self._ostokset
        )
        self._ostokset = list(ostokset)
