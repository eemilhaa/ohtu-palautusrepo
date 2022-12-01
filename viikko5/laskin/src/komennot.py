class Operaatio:
    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self._lue_syote = lue_syote


class Summa(Operaatio):
    def __init__(self, sovellus, lue_syote):
        super().__init__(sovellus, lue_syote)

    def suorita(self):
        arvo = self._lue_syote()
        self._sovellus.plus(arvo)


class Erotus(Operaatio):
    def __init__(self, sovellus, lue_syote):
        super().__init__(sovellus, lue_syote)

    def suorita(self):
        arvo = self._lue_syote()
        self._sovellus.miinus(arvo)


class Nollaus(Operaatio):
    def __init__(self, sovellus, lue_syote):
        super().__init__(sovellus, lue_syote)

    def suorita(self):
        self._sovellus.nollaa()


class Kumoa(Operaatio):
    def __init__(self, sovellus, lue_syote):
        super().__init__(sovellus, lue_syote)

    def suorita(self):
        pass