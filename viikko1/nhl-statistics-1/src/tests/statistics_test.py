import unittest

from statistics import Statistics
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_returns_correct_players_when_found(self):
        search_name = "Semenko"
        result = self.statistics.search(name=search_name)
        self.assertEqual(result.name, search_name)

    def test_search_returns_none_when_not_found(self):
        search_name = "asdf"
        result = self.statistics.search(name=search_name)
        self.assertIsNone(result)

    def test_team_search_returns_correct_players(self):
        search_name = "EDM"
        result = self.statistics.team(team_name=search_name)
        names = [player.name for player in result]
        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_top_returns_correct_players(self):
        result = self.statistics.top(how_many=0)
        names = [player.name for player in result]
        self.assertEqual(names, ["Gretzky"])
