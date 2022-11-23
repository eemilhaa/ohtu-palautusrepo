import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            saldot = {
                1: 10,
                2: 2,
                3: 3,
                4: 0,
            }
            return saldot[tuote_id]

        def varasto_hae_tuote(tuote_id):
            tuotteet = {
                1: Tuote(1, "maito", 5),
                2: Tuote(2, "juusto", 6),
                3: Tuote(2, "leipä", 3),
                4: Tuote(2, "nakki", 10),
            }
            return tuotteet[tuote_id]

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.kauppa = Kauppa(
            self.varasto_mock,
            self.pankki_mock,
            self.viitegeneraattori_mock
        )

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called()

    def test_yksi_tuote_tilisiirto_kutsuttu_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", self.kauppa._kaupan_tili, 5
        )

    def test_kaksi_eri_tuotetta_tilisiirto_kutsuttu_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", self.kauppa._kaupan_tili, 11
        )

    def test_kaksi_samaa_tuotetta_tilisiirto_kutsuttu_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", self.kauppa._kaupan_tili, 6
        )

    def test_kaksi_tuotetta_toinen_loppu_tilisiirto_kutsuttu_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.lisaa_koriin(4)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", self.kauppa._kaupan_tili, 3
        )
