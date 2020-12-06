from unittest import TestCase
from unittest.mock import patch
from yahtzee import roll_die


class TestRollDie(TestCase):
    @patch('random.randint', side_effect=[1, 2, 3, 4, 5])
    @patch('random.randint', return_value=[1, 2, 3, 4, 5])
    def test_roll_die_empty_list(self):
        result = roll_die([])
        expected = [1, 2, 3, 4, 5]

        self.assertEqual(result, expected)

    @patch('random.randint', side_effect=[3, 4, 2, 3, 1])
    @patch('random.randint', return_value=[3, 4, 2, 3, 1])
    def test_roll_die_1_in_list(self):
        result = roll_die([3])
        expected = [3, 4, 2, 3, 1]

        self.assertEqual(result, expected)

    @patch('random.randint', side_effect=[3, 6, 1, 1, 1])
    @patch('random.randint', return_value=[3, 6, 1, 1, 1])
    def test_roll_die_2_in_list(self):
        result = roll_die([3, 6])
        expected = [3, 6, 1, 1, 1]

        self.assertEqual(result, expected)

    @patch('random.randint', side_effect=[3, 6, 5, 2, 1])
    @patch('random.randint', return_value=[3, 6, 5, 2, 1])
    def test_roll_die_3_in_list(self):
        result = roll_die([3, 6, 5])
        expected = [3, 6, 5, 2, 1]

        self.assertEqual(result, expected)

    @patch('random.randint', side_effect=[3, 6, 5, 1, 4])
    @patch('random.randint', return_value=[3, 6, 5, 1, 4])
    def test_roll_die_4_in_list(self):
        result = roll_die([3, 6, 5, 1])
        expected = [3, 6, 5, 1, 4]

        self.assertEqual(result, expected)