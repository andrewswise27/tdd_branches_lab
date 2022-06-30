import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    def setUp(self):
        self.results = {
            "Home Win": {"Home": 2, "Away": 1},
            "Away Win": {"Home": 1, "Away": 2},
            "Draw": {"Home": 2, "Away": 2}
        }
        
        

    def test_home_win_returns_home_win_string(self):
        self.assertEqual("Home Win", get_result(self.results["Home Win"]))
        
    def test_away_win_returns_away_win_string(self):
        self.assertEqual("Away Win", get_result(self.results["Away Win"]))

    def test_draw_returns_draw_string(self):
        self.assertEqual("Draw", get_result(self.results["Draw"]))

    def test_return_list_of_result_strings(self):
        self.assertEqual(["Home Win", "Away Win", "Draw"], get_results(self.results))

    
    # Test we get the right result string for a final score dictionary representing -

        # Home win
        # Away win
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 



