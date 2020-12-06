import io
from unittest import TestCase
from unittest.mock import patch
from yahtzee import print_score


class TestPrintScore(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_score(self, mock_output):
        scorecard = {"Aces": 1, "Twos": 2, "Threes": 3, "Fours": 4, "Fives": 5, "Sixes": 6,
                     "Three Of A Kind": 17, "Four Of A Kind": 24, "Full House": 25,
                     "Small Straight": 30, "Large Straight": 40, "Yahtzee": 50, "Chance": 10}
        print_score(scorecard)
        print_score_printed_this = mock_output.getvalue()
        expected_output = "Aces\t1\nTwos\t2\nThrees\t3\nFours\t4\nFives\t5\nSixes\t6\n\
                          Three Of A Kind\t17\nFour Of A Kind\t24\nFull House\t25\nSmall Straight\
                          \t30\nLarge Straight\t40\nYahtzee\t50\nChance\t10"

        self.assertEqual(expected_output, print_score_printed_this)
