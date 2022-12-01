class Operaatio:
    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self._lue_syote = lue_syote
        self._edelliset_arvot = []

    def kumoa(self):
        edellinen_arvo = self._edelliset_arvot.pop(-1)
        self._sovellus.aseta_arvo(edellinen_arvo)


class Summa(Operaatio):
    def __init__(self, sovellus, lue_syote):
        super().__init__(sovellus, lue_syote)

    def suorita(self):
        self._edelliset_arvot.append(self._sovellus.tulos)
        arvo = self._lue_syote()
        self._sovellus.plus(arvo)


class Erotus(Operaatio):
    def __init__(self, sovellus, lue_syote):
        super().__init__(sovellus, lue_syote)

    def suorita(self):
        self._edelliset_arvot.append(self._sovellus.tulos)
        arvo = self._lue_syote()
        self._sovellus.miinus(arvo)


class Nollaus(Operaatio):
    def __init__(self, sovellus, lue_syote):
        super().__init__(sovellus, lue_syote)

    def suorita(self):
        self._edelliset_arvot.append(self._sovellus.tulos)
        self._sovellus.nollaa()


class Kumoa:
    def __init__(self, sovellus, lue_syote, komentohistoria: list):
        self._sovellus = sovellus
        self._lue_syote = lue_syote
        self._komentohistoria = komentohistoria

    def suorita(self):
        kumottava_komento = self._komentohistoria.pop(-1)
        kumottava_komento.kumoa()
