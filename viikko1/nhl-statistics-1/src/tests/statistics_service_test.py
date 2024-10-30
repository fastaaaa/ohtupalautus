import unittest
from statistics_service import StatisticsService, SortBy
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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        result = self.stats.search("Kurri")
        self.assertEqual(result.name, "Kurri")

    def test_top_players(self):
        result = self.stats.top(2)
        self.assertEqual(result[0].name, "Gretzky")
        self.assertEqual(result[1].name, "Lemieux")

    def test_team(self):
        result = self.stats.team("EDM")
        self.assertEqual(result[0].name, "Semenko")
        self.assertEqual(result[1].name, "Kurri")
        self.assertEqual(result[2].name, "Gretzky")

    def test_search_wrong_name(self):
        result = self.stats.search("Karri")
        self.assertEqual(result, None)


    def test_top_players_goals(self):
        result = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(result[0].name, "Lemieux")
        self.assertEqual(result[1].name, "Yzerman")

    def test_top_players_assists(self):
        result = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(result[0].name, "Gretzky")
        self.assertEqual(result[1].name, "Yzerman")
        


