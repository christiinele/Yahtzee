import io
from unittest import TestCase
from unittest.mock import patch
from yahtzee import print_current_dice


class TestPrintScore(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_current_dice_5(self, mock_output):
        current_dice = [1, 2, 3, 4, 5]
        print_current_dice(current_dice)
        print_score_printed_this = mock_output.getvalue()
        expected_output = "1\t2\t3\t4\t5"

        self.assertEqual(expected_output, print_score_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_current_dice_4(self, mock_output):
        current_dice = [3, 4, 4, 1]
        print_current_dice(current_dice)
        print_score_printed_this = mock_output.getvalue()
        expected_output = "3\t4\t4\t1"

        self.assertEqual(expected_output, print_score_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_current_dice_3(self, mock_output):
        current_dice = [2, 6, 1]
        print_current_dice(current_dice)
        print_score_printed_this = mock_output.getvalue()
        expected_output = "2\t6\t1"

        self.assertEqual(expected_output, print_score_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_current_dice_2(self, mock_output):
        current_dice = [2, 2]
        print_current_dice(current_dice)
        print_score_printed_this = mock_output.getvalue()
        expected_output = "2\t2"

        self.assertEqual(expected_output, print_score_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_current_dice_1(self, mock_output):
        current_dice = [5]
        print_current_dice(current_dice)
        print_score_printed_this = mock_output.getvalue()
        expected_output = "5"

        self.assertEqual(expected_output, print_score_printed_this)
