from unittest import TestCase
from yahtzee import validate_combo


class TestValidateCombo(TestCase):
    def test_validate_combo_ones_true(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = "1"
        expected = True
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_ones_false(self):
        current_dice = [2, 3, 5, 3, 2]
        combo_choice = "1"
        expected = False
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_twos_true(self):
        current_dice = [2, 2, 2, 2, 2]
        combo_choice = "2"
        expected = True
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_twos_false(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = "2"
        expected = False
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_threes_true(self):
        current_dice = [3, 3, 3, 3, 3]
        combo_choice = "3"
        expected = True
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_threes_false(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = "3"
        expected = False
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_fours_true(self):
        current_dice = [4, 4, 4, 4, 4]
        combo_choice = "4"
        expected = True
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_fours_false(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = "4"
        expected = False
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_fives_true(self):
        current_dice = [5, 5, 5, 5, 5]
        combo_choice = "5"
        expected = True
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_fives_false(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = "5"
        expected = False
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_sixes_true(self):
        current_dice = [6, 6, 6, 6, 6]
        combo_choice = "6"
        expected = True
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_sixes_false(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = "6"
        expected = False
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_three_of_a_kind_1(self):
        current_dice = [1, 1, 1, 2, 5]
        combo_choice = "7"
        expected = True
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_three_of_a_kind_2(self):
        current_dice = [1, 1, 1, 1, 4]
        combo_choice = "7"
        expected = True
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_three_of_a_kind_3(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = "7"
        expected = True
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_three_of_a_kind_false(self):
        current_dice = [2, 1, 4, 6, 4]
        combo_choice = "7"
        expected = False
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_four_of_a_kind_1(self):
        current_dice = [1, 1, 1, 1, 2]
        combo_choice = "8"
        expected = True
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_four_of_a_kind_2(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = "8"
        expected = True
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_four_of_a_kind_false(self):
        current_dice = [1, 4, 3, 2, 2]
        combo_choice = "8"
        expected = False
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_full_house_true(self):
        current_dice = [1, 1, 1, 3, 3]
        combo_choice = "9"
        expected = True
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_full_house_false(self):
        current_dice = [4, 3, 2, 1, 3]
        combo_choice = "9"
        expected = False
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_small_straight_1(self):
        current_dice = [1, 2, 3, 4, 5]
        combo_choice = "10"
        expected = True
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_small_straight_2(self):
        current_dice = [1, 2, 3, 4, 6]
        combo_choice = "10"
        expected = True
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_small_straight_false(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = "10"
        expected = False
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_large_straight_true(self):
        current_dice = [1, 2, 3, 4, 5]
        combo_choice = "11"
        expected = True
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_large_straight_false(self):
        current_dice = [1, 2, 3, 4, 6]
        combo_choice = "11"
        expected = False
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_yahtzee_true(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = "12"
        expected = True
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_yahtzee_false(self):
        current_dice = [1, 1, 1, 1, 2]
        combo_choice = "12"
        expected = False
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)

    def test_validate_combo_chance(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = "13"
        expected = True
        actual = validate_combo(current_dice, combo_choice)

        self.assertEqual(expected, actual)