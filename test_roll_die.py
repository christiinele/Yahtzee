from unittest import TestCase
from unittest.mock import patch
from yahtzee import roll_die

# at this point my head hurts


class TestRollDie(TestCase):
    @patch('random.randrange', side_effect=[1, 2, 3, 4, 5])
    def test_roll_die_empty_list(self, mock):
        roll_die([])
        result = mock.getvalue()
        expected = [1, 2, 3, 4, 5]

        self.assertEqual(result, expected)
