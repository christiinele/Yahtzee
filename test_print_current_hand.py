import io
from unittest import TestCase
from unittest.mock import patch
from yahtzee import print_current_hand


class TestPrintCurrentHand(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_current_dice_5(self, mock_output):
        current_dice = [1, 2, 3, 4, 5]
        print_current_hand(current_dice)
        print_score_printed_this = mock_output.getvalue()
        expected_output = "[ 1 ]\t[ 2 ]\t[ 3 ]\t[ 4 ]\t[ 5 ]\t"

        self.assertEqual(expected_output, print_score_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_current_dice_4(self, mock_output):
        current_dice = [3, 4, 4, 1]
        print_current_hand(current_dice)
        print_score_printed_this = mock_output.getvalue()
        expected_output = "[ 3 ]\t[ 4 ]\t[ 4 ]\t[ 1 ]\t"

        self.assertEqual(expected_output, print_score_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_current_dice_3(self, mock_output):
        current_dice = [2, 6, 1]
        print_current_hand(current_dice)
        print_score_printed_this = mock_output.getvalue()
        expected_output = "[ 2 ]\t[ 6 ]\t[ 1 ]\t"

        self.assertEqual(expected_output, print_score_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_current_dice_2(self, mock_output):
        current_dice = [2, 2]
        print_current_hand(current_dice)
        print_score_printed_this = mock_output.getvalue()
        expected_output = "[ 2 ]\t[ 2 ]\t"

        self.assertEqual(expected_output, print_score_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_current_dice_1(self, mock_output):
        current_dice = [5]
        print_current_hand(current_dice)
        print_score_printed_this = mock_output.getvalue()
        expected_output = "[ 5 ]\t"

        self.assertEqual(expected_output, print_score_printed_this)
