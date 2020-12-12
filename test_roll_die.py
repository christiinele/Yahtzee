from unittest import TestCase
from unittest.mock import patch
from yahtzee import roll_die


class TestRollDie(TestCase):

    @patch('random.choices', return_value=[1, 2, 3, 4, 5])
    def test_roll_die_empty_list(self, mock):
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(roll_die([]), expected)

    @patch('random.choices', return_value=[2, 3, 4, 5])
    def test_roll_die_list_1(self, mock):
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(roll_die([1]), expected)

    @patch('random.choices', return_value=[3, 4, 5])
    def test_roll_die_list_2(self, mock):
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(roll_die([1, 2]), expected)

    @patch('random.choices', return_value=[4, 5])
    def test_roll_die_list_3(self, mock):
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(roll_die([1, 2, 3]), expected)

    @patch('random.choices', return_value=[5])
    def test_roll_die_list_4(self, mock):
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(roll_die([1, 2, 3, 4]), expected)
