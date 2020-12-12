from unittest import TestCase
from yahtzee import calculate_score


class TestCalculateScore(TestCase):
    def test_calculate_score_1(self):
        scorecard = {"Ones": 1, "Twos": 2, "Threes": 3, "Fours": 4, "Fives": 5, "Sixes": 6,
                     "Three Of A Kind": 17, "Four Of A Kind": 24, "Full House": 25,
                     "Small Straight": 30, "Large Straight": 40, "Yahtzee": 50, "Chance": 10}
        result = calculate_score(scorecard)
        expected = 217

        self.assertEqual(result, expected)

    def test_calculate_score_2(self):
        scorecard = {"Ones": 0, "Twos": 2, "Threes": 3, "Fours": 4, "Fives": 5, "Sixes": 6,
                     "Three Of A Kind": 17, "Four Of A Kind": 24, "Full House": 25,
                     "Small Straight": 30, "Large Straight": 0, "Yahtzee": 50, "Chance": 10}
        result = calculate_score(scorecard)
        expected = 176

        self.assertEqual(result, expected)

    def test_calculate_score_3(self):
        scorecard = {"Ones": 5, "Twos": 10, "Threes": 15, "Fours": 20, "Fives": 25, "Sixes": 30,
                     "Three Of A Kind": 17, "Four Of A Kind": 24, "Full House": 25,
                     "Small Straight": 30, "Large Straight": 40, "Yahtzee": 50, "Chance": 10}
        result = calculate_score(scorecard)
        expected = 336

        self.assertEqual(result, expected)
