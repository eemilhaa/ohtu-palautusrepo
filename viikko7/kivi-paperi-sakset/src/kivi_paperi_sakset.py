from tuomari import default_tuomari
from console_io import default_console_io


SALLITUT_SIIRROT = ("k", "s", "p")


class KiviPaperiSakset:
    def __init__(self, tuomari=default_tuomari, io=default_console_io):
        self._tuomari = tuomari
        self._io = io

    def pelaa(self):
        while True:
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)
            if not self._onko_ok_siirrot(ekan_siirto, tokan_siirto):
                break
            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            self._io.write(self._tuomari.ilmoita_tilanne())
        self._lopeta_peli()

    def _ensimmaisen_siirto(self):
        return self._io.read("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirrot(self, *siirrot):
        for siirto in siirrot:
            if siirto in SALLITUT_SIIRROT:
                return True
            return False

    def _lopeta_peli(self):
        self._io.write("Kiitos!")
        self._io.write(self._tuomari.ilmoita_tilanne())
        self._tuomari.nollaa()
