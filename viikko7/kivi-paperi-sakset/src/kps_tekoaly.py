from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly import default_tekoaly


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self, tekoaly=default_tekoaly):
        super().__init__()
        self._tekoaly = tekoaly

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self._tekoaly.anna_siirto()
        self._io.write(f"Tietokone valitsi: {siirto}")
        return siirto
