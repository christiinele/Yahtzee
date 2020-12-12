import io
from unittest import TestCase
from unittest.mock import patch
from yahtzee import game_verdict


class TestGameVerdict(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_verdict_player_1_wins(self, mock_output):
        game_verdict(150, 100, 200, 0)
        game_verdict_printed_this = mock_output.getvalue()
        expected_output = "\n\nPlayer one is the winner with a score of 250 to 200!\n"

        self.assertEqual(expected_output, game_verdict_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_verdict_player_2_wins(self, mock_output):
        game_verdict(200, 0, 201, 0)
        game_verdict_printed_this = mock_output.getvalue()
        expected_output = "\n\nPlayer two is the winner with a score of 201 to 200!\n"

        self.assertEqual(expected_output, game_verdict_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_verdict_players_tied(self, mock_output):
        game_verdict(300, 0, 300, 0)
        game_verdict_printed_this = mock_output.getvalue()
        expected_output = "\n\nBoth players got a score of: 300. The players tied!\n"

        self.assertEqual(expected_output, game_verdict_printed_this)