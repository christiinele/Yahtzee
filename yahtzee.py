"""
Christine Le
A01235924
Final - Yahtzee
"""


import random


def create_score_card() -> dict:
    """ Create a score card.

    Generates a score card that can be updated with the players' scores as the game progresses.

    :return: dictionary with players' scores
    """

    score_card = {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                  "Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1,
                  "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1}

    return score_card


def print_score(score_card: dict):
    """ Print score card.

    Display players' current scored combos and sum of their scores.

    :precondition: dictionary needs to be initialized with keys and values, even if values are empty
    :postcondition: displays players' scores in a readable format
    """

    for key, value in score_card.items():
        print(f"{key}\t{value}")


def roll_die(current_die: list) -> list:
    """ Roll die.

    Depending on how many dice are in the current list, roll up to five new dice and return the
    results.

    :param current_die: list of how many dice the player has kept
    :precondition: passed parameter must be a list with integers or empty spaces
    :postcondition: fills out the empty fields in the list with integers from 1-6
    :return: list of die
    """

    if len(current_die) < 5:
        for dice in range(5 - len(current_die)):
            current_die.append(random.randrange(1, 7))

    return current_die


def select_die(current_die: list) -> list:
    """ Choose die to keep.

    Discards die the player doesn't want to keep and keeps going until the player is satisfied.

    :param current_die: list of dice the user currently has
    :precondition: parameter is a list of integers that can be popped
    :postcondition: creates a new list of dice that the user wants to keep
    :return: list of dice the user has chosen to keep
    """

    return None


def print_current_dice(current_die: list):
    """ Print die.

    Taking the list of current dice the player has, prints it in a readable format for the player.

    :param current_die: list of dice the player currently has
    :precondition: passed parameter must be a list
    :postcondition: prints list in the command line for the player in a readable format
    """

    return None


def validate_combo(current_dice: list, combo_choice: str) -> int:
    """ Check dice combination.

    Taking what combo choice the user has selected, checks to see if it is valid and if so, returns
    the value of the combo. If it is invalid, the user gets a 0.

    :param current_dice: list of dice the player currently has
    :param combo_choice: string that is a number which indicates which combo the user wants to
    select
    :precondition: list must contain integers from 1-6, combo choice must be a valid string
    :return: value of combo that player has selected
    """

    return None


def update_score(scorecard: dict, combo_to_update: str, combo_value: int) -> dict:
    """ Update player score.

    Updates the dictionary with players' scores with the value of the combo they selected.

    :param scorecard: dictionary of possible combos and what the player has scored thus far
    :param combo_to_update: string to indicate which key to update with a value
    :param combo_value: integer value for the key the player wants to update
    :precondition: scorecard has been initialized with proper keys, the combo to update exists as a
    pre-existing key, and combo value is equal to or more than zero
    :return: updated dictionary with the player's new score
    """

    return None


def check_bonus(scorecard: dict) -> bool:
    """ Check for bonus.

    Sums up the upper section of the player's scorecard and checks whether it is equal to or
    greater 63.

    :param scorecard: dictionary containing player's current scores
    :precondition: parameter passed is the dictionary containing player's current scores
    :postcondition: checks whether their upper section reaches the threshold for a bonus
    :return: boolean if the player has already gotten Yahtzee or not
    """

    return None


def initialize_game():
    """
    Print interface for players to start the game.
    """

    pass


def main():
    """
    Drives the program
    """

    initialize_game()


if __name__ == "__main__":
    main()
