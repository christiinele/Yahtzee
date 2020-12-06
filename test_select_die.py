import io
from unittest import TestCase
from unittest.mock import patch
from yahtzee import select_die


class TestSelectDie(TestCase):
    @patch('builtins.input', side_effect=["0"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_die_index_0(self, mock_input):
        current_die = [1, 2, 3, 4, 5]
        result = select_die(current_die)
        expected = [2, 3, 4, 5]

        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=["1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_die_index_1(self, mock_input):
        current_die = [1, 2, 3, 4, 5]
        result = select_die(current_die)
        expected = [1, 3, 4, 5]

        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=["2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_die_index_2(self, mock_input):
        current_die = [1, 2, 3, 4, 5]
        result = select_die(current_die)
        expected = [1, 2, 4, 5]

        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=["3"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_die_index_3(self, mock_input):
        current_die = [1, 2, 3, 4, 5]
        result = select_die(current_die)
        expected = [1, 2, 3, 5]

        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=["4"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_die_index_4(self, mock_input):
        current_die = [1, 2, 3, 4, 5]
        result = select_die(current_die)
        expected = [1, 2, 3, 4]

        self.assertEqual(result, expected)
