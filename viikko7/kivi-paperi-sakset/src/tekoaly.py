from itertools import cycle
from kivi_paperi_sakset import SALLITUT_SIIRROT


class Tekoaly:
    def __init__(self, siirrot=SALLITUT_SIIRROT):
        self._siirrot = cycle(siirrot)

    def anna_siirto(self):
        return next(self._siirrot)

    def aseta_siirto(self, siirto):
        # ei tehdä mitään
        pass

    def nollaa(self):
        # ei tehdä mitään
        pass


default_tekoaly = Tekoaly()
