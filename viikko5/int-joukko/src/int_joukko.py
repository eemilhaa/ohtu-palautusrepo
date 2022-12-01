KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.taulukko = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        if n in self.taulukko:
            return True
        return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.taulukko[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            if self.alkioiden_lkm == len(self.taulukko):
                self._luo_suurempi_taulukko()
            return True
        return False

    def _luo_suurempi_taulukko(self):
        [self.taulukko.append(0) for _ in range(self.kasvatuskoko)]

    def poista(self, n):
        if self.kuuluu(n):
            self.taulukko.remove(n)
            self.alkioiden_lkm -= 1
            return True
        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return [luku for luku in self.taulukko if luku != 0]

    def yhdiste(a, b):
        yhdiste = IntJoukko()
        [yhdiste.lisaa(luku) for luku in a.taulukko + b.taulukko]
        return yhdiste

    def leikkaus(a, b):
        leikkaus = IntJoukko()
        for luku in a.taulukko + b.taulukko:
            if a.kuuluu(luku) and b.kuuluu(luku):
                leikkaus.lisaa(luku)
        return leikkaus

    def erotus(a, b):
        erotus = IntJoukko()
        [erotus.lisaa(luku) for luku in a.taulukko if not b.kuuluu(luku)]
        return erotus

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        return f"{set(self.to_int_list())}"
