from unittest import TestCase
from yahtzee import check_bonus


class TestCheckBonus(TestCase):
    def test_check_bonus_false(self):
        scorecard = {"Aces": 1, "Twos": 2, "Threes": 3, "Fours": 4, "Fives": 5, "Sixes": 6,
                     "Three Of A Kind": 17, "Four Of A Kind": 24, "Full House": 25,
                     "Small Straight": 30, "Large Straight": 40, "Yahtzee": 50, "Chance": 10}
        result = check_bonus(scorecard)
        expected = False

        self.assertEqual(result, expected)

    def test_check_bonus_true_1(self):
        scorecard = {"Aces": 5, "Twos": 10, "Threes": 15, "Fours": 20, "Fives": 25, "Sixes": 30,
                     "Three Of A Kind": 17, "Four Of A Kind": 24, "Full House": 25,
                     "Small Straight": 30, "Large Straight": 40, "Yahtzee": 50, "Chance": 10}
        result = check_bonus(scorecard)
        expected = True

        self.assertEqual(result, expected)

    def test_check_bonus_true_2(self):
        scorecard = {"Aces": 4, "Twos": 2, "Threes": 3, "Fours": 4, "Fives": 20, "Sixes": 30,
                     "Three Of A Kind": 17, "Four Of A Kind": 24, "Full House": 25,
                     "Small Straight": 30, "Large Straight": 40, "Yahtzee": 50, "Chance": 10}
        result = check_bonus(scorecard)
        expected = True

        self.assertEqual(result, expected)
