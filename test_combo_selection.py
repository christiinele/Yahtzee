from unittest import TestCase
from yahtzee import combo_selection


class TestValidateCombo(TestCase):
    def test_combo_selection_ones_true(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = 1
        expected = 5
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_ones_false(self):
        current_dice = [2, 3, 5, 3, 2]
        combo_choice = 1
        expected = 0
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_twos_true(self):
        current_dice = [2, 2, 2, 2, 2]
        combo_choice = 2
        expected = 10
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_twos_false(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = 2
        expected = 0
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_threes_true(self):
        current_dice = [3, 3, 3, 3, 3]
        combo_choice = 3
        expected = 15
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_threes_false(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = 3
        expected = 0
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_fours_true(self):
        current_dice = [4, 4, 4, 4, 4]
        combo_choice = 4
        expected = 20
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_fours_false(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = 4
        expected = 0
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_fives_true(self):
        current_dice = [5, 5, 5, 5, 5]
        combo_choice = 5
        expected = 25
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_fives_false(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = 5
        expected = 0
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_sixes_true(self):
        current_dice = [6, 6, 6, 6, 6]
        combo_choice = 6
        expected = 30
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_sixes_false(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = 6
        expected = 0
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_three_of_a_kind_1(self):
        current_dice = [2, 3, 4, 4, 4]
        combo_choice = 7
        expected = 17
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_three_of_a_kind_2(self):
        current_dice = [1, 1, 1, 1, 4]
        combo_choice = 7
        expected = 8
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_three_of_a_kind_3(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = 7
        expected = 5
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_three_of_a_kind_false(self):
        current_dice = [2, 1, 4, 6, 4]
        combo_choice = 7
        expected = 0
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_four_of_a_kind_1(self):
        current_dice = [1, 1, 1, 1, 2]
        combo_choice = 8
        expected = 6
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_four_of_a_kind_2(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = 8
        expected = 5
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_four_of_a_kind_false(self):
        current_dice = [1, 4, 3, 2, 2]
        combo_choice = 8
        expected = 0
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_full_house_true(self):
        current_dice = [1, 1, 3, 1, 3]
        combo_choice = 9
        expected = 25
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_full_house_false(self):
        current_dice = [4, 3, 2, 1, 3]
        combo_choice = 9
        expected = 0
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_small_straight_1(self):
        current_dice = [1, 2, 3, 4, 5]
        combo_choice = 10
        expected = 30
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_small_straight_2(self):
        current_dice = [1, 2, 3, 4, 6]
        combo_choice = 10
        expected = 30
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_small_straight_false(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = 10
        expected = 0
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_large_straight_true(self):
        current_dice = [1, 2, 3, 4, 5]
        combo_choice = 11
        expected = 40
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_large_straight_false(self):
        current_dice = [1, 2, 3, 4, 6]
        combo_choice = 11
        expected = 0
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_yahtzee_true(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = 12
        expected = 50
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_yahtzee_false(self):
        current_dice = [1, 1, 1, 1, 2]
        combo_choice = 12
        expected = 0
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)

    def test_combo_selection_chance(self):
        current_dice = [1, 1, 1, 1, 1]
        combo_choice = 13
        expected = 5
        actual = combo_selection(combo_choice, current_dice)

        self.assertEqual(expected, actual)