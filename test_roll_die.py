from unittest import TestCase
from unittest.mock import patch
from yahtzee import roll_die


class TestRollDie(TestCase):
    @patch('random.randrange', return_value=1)
    @patch('random.randrange', return_value=2)
    @patch('random.randrange', return_value=3)
    @patch('random.randrange', return_value=4)
    @patch('random.randrange', return_value=5)
    def test_roll_die_empty_list(self, mock):
        result = roll_die([mock.getvalue()])
        expected = [1, 2, 3, 4, 5]

        self.assertEqual(result, expected)
