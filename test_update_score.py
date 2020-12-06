from unittest import TestCase
from yahtzee import update_score


class TestUpdateScore(TestCase):
    def test_update_score_ones(self):
        scorecard = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                     "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                     "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}
        combo_to_update = "Ones"
        combo_value = 3
        actual = update_score(scorecard, combo_to_update, combo_value)
        expected = {"Ones": 3, "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                    "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                    "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}

        self.assertEqual(expected, actual)

    def test_update_score_twos(self):
        scorecard = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                     "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                     "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}
        combo_to_update = "Twos"
        combo_value = 4
        actual = update_score(scorecard, combo_to_update, combo_value)
        expected = {"Ones": "", "Twos": 4, "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                    "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                    "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}

        self.assertEqual(expected, actual)

    def test_update_score_threes(self):
        scorecard = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                     "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                     "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}
        combo_to_update = "Threes"
        combo_value = 9
        actual = update_score(scorecard, combo_to_update, combo_value)
        expected = {"Ones": "", "Twos": "", "Threes": 9, "Fours": "", "Fives": "", "Sixes": "",
                    "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                    "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}

        self.assertEqual(expected, actual)

    def test_update_score_fours(self):
        scorecard = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                     "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                     "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}
        combo_to_update = "Fours"
        combo_value = 4
        actual = update_score(scorecard, combo_to_update, combo_value)
        expected = {"Ones": "", "Twos": "", "Threes": "", "Fours": 4, "Fives": "", "Sixes": "",
                    "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                    "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}

        self.assertEqual(expected, actual)

    def test_update_score_fives(self):
        scorecard = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                     "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                     "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}
        combo_to_update = "Fives"
        combo_value = 25
        actual = update_score(scorecard, combo_to_update, combo_value)
        expected = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": 25, "Sixes": "",
                    "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                    "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}

        self.assertEqual(expected, actual)

    def test_update_score_sixes(self):
        scorecard = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                     "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                     "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}
        combo_to_update = "Sixes"
        combo_value = 6
        actual = update_score(scorecard, combo_to_update, combo_value)
        expected = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": 6,
                    "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                    "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}

        self.assertEqual(expected, actual)

    def test_update_score_three_of_a_kind(self):
        scorecard = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                     "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                     "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}
        combo_to_update = "Three Of A Kind"
        combo_value = 17
        actual = update_score(scorecard, combo_to_update, combo_value)
        expected = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                    "Three Of A Kind": 17, "Four Of A Kind": "", "Full House": "",
                    "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}

        self.assertEqual(expected, actual)

    def test_update_score_four_of_a_kind(self):
        scorecard = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                     "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                     "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}
        combo_to_update = "Four Of A Kind"
        combo_value = 24
        actual = update_score(scorecard, combo_to_update, combo_value)
        expected = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                    "Three Of A Kind": "", "Four Of A Kind": 24, "Full House": "",
                    "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}

        self.assertEqual(expected, actual)

    def test_update_score_full_house(self):
        scorecard = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                     "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                     "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}
        combo_to_update = "Full House"
        combo_value = 25
        actual = update_score(scorecard, combo_to_update, combo_value)
        expected = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                    "Three Of A Kind": "", "Four Of A Kind": "", "Full House": 25,
                    "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}

        self.assertEqual(expected, actual)

    def test_update_score_small_straight(self):
        scorecard = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                     "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                     "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}
        combo_to_update = "Small Straight"
        combo_value = 30
        actual = update_score(scorecard, combo_to_update, combo_value)
        expected = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                    "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                    "Small Straight": 30, "Large Straight": "", "Yahtzee": "", "Chance": ""}

        self.assertEqual(expected, actual)

    def test_update_score_large_straight(self):
        scorecard = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                     "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                     "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}
        combo_to_update = "Large Straight"
        combo_value = 40
        actual = update_score(scorecard, combo_to_update, combo_value)
        expected = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                    "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                    "Small Straight": "", "Large Straight": 40, "Yahtzee": "", "Chance": ""}

        self.assertEqual(expected, actual)

    def test_update_score_yahtzee(self):
        scorecard = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                     "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                     "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}
        combo_to_update = "Yahtzee"
        combo_value = 50
        actual = update_score(scorecard, combo_to_update, combo_value)
        expected = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                    "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                    "Small Straight": "", "Large Straight": "", "Yahtzee": 50, "Chance": ""}

        self.assertEqual(expected, actual)

    def test_update_score_(self):
        scorecard = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                     "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                     "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": ""}
        combo_to_update = "Chance"
        combo_value = 10
        actual = update_score(scorecard, combo_to_update, combo_value)
        expected = {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                    "Three Of A Kind": "", "Four Of A Kind": "", "Full House": "",
                    "Small Straight": "", "Large Straight": "", "Yahtzee": "", "Chance": 10}

        self.assertEqual(expected, actual)
