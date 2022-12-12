from tuomari import default_tuomari


class KiviPaperiSakset:
    def __init__(self, tuomari=default_tuomari):
        self._tuomari = tuomari

    def pelaa(self):
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)
        while self._onko_ok_siirrot(ekan_siirto, tokan_siirto):
            pass
        print("Kiitos!")
        print(self._tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirrot(self, *siirrot):
        for siirto in siirrot:
            if siirto == "k" or siirto == "p" or siirto == "s":
                return True
            return False
