from unittest import TestCase
from yahtzee import update_score


class TestUpdateScore(TestCase):
    def test_update_score_ones(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Ones"
        combo_value = 3
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = True

        self.assertEqual(expected, actual)

    def test_update_score_ones_false(self):
        score_card = {"Ones": 2, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Ones"
        combo_value = 3
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = False

        self.assertEqual(expected, actual)

    def test_update_score_twos(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Twos"
        combo_value = 4
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = True

        self.assertEqual(expected, actual)

    def test_update_score_twos_false(self):
        score_card = {"Ones": -1, "Twos": 4, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Twos"
        combo_value = 4
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = False

        self.assertEqual(expected, actual)

    def test_update_score_threes(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Threes"
        combo_value = 9
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = True

        self.assertEqual(expected, actual)

    def test_update_score_threes_false(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": 9, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Threes"
        combo_value = 9
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = False

        self.assertEqual(expected, actual)

    def test_update_score_fours(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Fours"
        combo_value = 4
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = True

        self.assertEqual(expected, actual)

    def test_update_score_fours_false(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": 16, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Fours"
        combo_value = 4
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = False

        self.assertEqual(expected, actual)

    def test_update_score_fives(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Fives"
        combo_value = 25
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = True

        self.assertEqual(expected, actual)

    def test_update_score_fives_false(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": 10, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Fives"
        combo_value = 25
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = False

        self.assertEqual(expected, actual)

    def test_update_score_sixes(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Sixes"
        combo_value = 6
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = True

        self.assertEqual(expected, actual)

    def test_update_score_sixes_false(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": 6, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Sixes"
        combo_value = 12
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = False

        self.assertEqual(expected, actual)

    def test_update_score_three_of_a_kind(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Three Of A Kind"
        combo_value = 17
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = True

        self.assertEqual(expected, actual)

    def test_update_score_three_of_a_kind_false(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": 17, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Three Of A Kind"
        combo_value = 17
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = False

        self.assertEqual(expected, actual)

    def test_update_score_four_of_a_kind(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Four Of A Kind"
        combo_value = 24
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = True

        self.assertEqual(expected, actual)

    def test_update_score_four_of_a_kind_false(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": 8, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Four Of A Kind"
        combo_value = 24
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = False

        self.assertEqual(expected, actual)

    def test_update_score_full_house(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Full House"
        combo_value = 25
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = True

        self.assertEqual(expected, actual)

    def test_update_score_full_house_false(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": 25,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Full House"
        combo_value = 25
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = False

        self.assertEqual(expected, actual)

    def test_update_score_small_straight(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Small Straight"
        combo_value = 30
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = True

        self.assertEqual(expected, actual)

    def test_update_score_small_straight(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": 30, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Small Straight"
        combo_value = 30
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = False

        self.assertEqual(expected, actual)

    def test_update_score_large_straight(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Large Straight"
        combo_value = 40
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = True

        self.assertEqual(expected, actual)

    def test_update_score_large_straight_false(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": 40, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Large Straight"
        combo_value = 40
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = False

        self.assertEqual(expected, actual)

    def test_update_score_yahtzee(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Yahtzee"
        combo_value = 50
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = True

        self.assertEqual(expected, actual)

    def test_update_score_yahtzee_none(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Yahtzee"
        combo_value = 50
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = True

        self.assertEqual(expected, actual)

    def test_update_score_yahtzee_value(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": 50, "Chance": -1}
        combo_to_update = "Yahtzee"
        combo_value = 50
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = False

        self.assertEqual(expected, actual)

    def test_update_score_chance(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}
        combo_to_update = "Chance"
        combo_value = 10
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = True

        self.assertEqual(expected, actual)

    def test_update_score_chance_false(self):
        score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, \
                      "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                      "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": 10}
        combo_to_update = "Chance"
        combo_value = 10
        actual = update_score(score_card, combo_to_update, combo_value, 0)
        expected = False

        self.assertEqual(expected, actual)
