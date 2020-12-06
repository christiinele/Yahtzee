from unittest import TestCase
from yahtzee import create_scorecard


class TestCreateScoreCard(TestCase):
    def test_create_scorecard(self):
        expected = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                    "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                    "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}
        actual = create_scorecard()

        self.assertEqual(expected, actual)
