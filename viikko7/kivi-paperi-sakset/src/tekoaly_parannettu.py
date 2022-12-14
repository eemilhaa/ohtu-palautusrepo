# "Muistava tekoäly"
class TekoalyParannettu:
    def __init__(self, muistin_koko=10):
        self._muisti = []
        self._muistin_koko = muistin_koko

    def aseta_siirto(self, siirto):
        if len(self._muisti) >= self._muistin_koko:
            self._muisti = self._muisti[1:]
        self._muisti.append(siirto)

    def anna_siirto(self):
        # Tehdään siirron valinta esimerkiksi seuraavasti;
        # - jos kiviä eniten, annetaan aina paperi
        # - jos papereita eniten, annetaan aina sakset
        # muulloin annetaan aina kivi
        if self._muisti.count("k") > max(
            self._muisti.count("p"), self._muisti.count("s")
        ):
            return "p"
        elif self._muisti.count("p") > max(
            self._muisti.count("s"), self._muisti.count("k")
        ):
            return "s"
        return "k"

    def nollaa(self):
        self._muisti = []


default_parannettu_tekoaly = TekoalyParannettu()
