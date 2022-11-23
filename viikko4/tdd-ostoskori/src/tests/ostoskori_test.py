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
