import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_oikea_hinta_yhden_tuotteen_lisaamisen_jalkeen(self):
        HINTA = 2
        leipa = Tuote("Leipä", HINTA)
        self.kori.lisaa_tuote(leipa)
        self.assertEqual(self.kori.hinta(), HINTA)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipä", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_oikea_hinta_kahden_tuotteen_lisaamisen_jalkeen(self):
        hinta_1 = 3
        hinta_2 = 2
        HINTA_YHTEENSA = hinta_1 + hinta_2
        maito = Tuote("Maito", hinta_1)
        leipa = Tuote("Leipä", hinta_2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)
        self.assertEqual(self.kori.hinta(), HINTA_YHTEENSA)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_oikea_hinta_kahden_saman_tuotteen_lisaamisen_jalkeen(self):
        hinta = 3
        HINTA_YHTEENSA = 2 * hinta
        maito = Tuote("Maito", hinta)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), HINTA_YHTEENSA)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipä", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        ostos = ostokset[0]
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostos.lukumaara(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_ostoksen_jolla_sama_nimi_kuin_tuotteella_ja_lukumaara_2(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        ostos = ostokset[0]
        self.assertEqual(ostos.lukumaara(), 2)
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")

    def test_korissa_kaksi_samaa_tuotetta_toinen_poistetaan_ostoksessa_jaljella_yksi_tuote(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        ostokset = self.kori.ostokset()
        ostos = ostokset[0]
        self.assertEqual(ostos.lukumaara(), 1)
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")

    def test_kori_tyhjentamisen_jalkeen_tyhja(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.tyhjenna()
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
