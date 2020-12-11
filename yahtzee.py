"""
Christine Le
A01235924
Final - Yahtzee
"""


import random
import re
import doctest


def list_to_string(die: list) -> str:
    string = ""

    for item in sorted(die):
        string += str(item)

    return string


def create_scorecard() -> dict:
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

    MAX_DIE_IN_LIST = 5
    MIN = 1
    MAX = 7

    if len(current_die) < MAX_DIE_IN_LIST:
        for dice in range(MAX_DIE_IN_LIST - len(current_die)):
            current_die.append(random.randrange(MIN, MAX))

    return current_die


def print_current_hand(die: list):
    """ Print die.

    Taking the list of current dice the player has, prints it in a readable format for the player.

    :param die: list of dice the player currently has
    :precondition: passed parameter must be a list
    :postcondition: prints list in the command line for the player in a readable format
    """

    for dice in die:
        print(f"[ {dice} ]\t", end='')


def remove_die(current_die: list) -> list:
    """ Choose die to remove.

    Discards die the player doesn't want to keep and keeps going until the player is satisfied.

    :param current_die: list of dice the user currently has
    :precondition: parameter is a list of integers that can be popped
    :postcondition: creates a new list of dice that the user wants to keep
    :return: list of dice the user has chosen to keep
    """

    dice_selection = True
    MIN = 0
    MAX = 5

    while dice_selection:
        for index in range(len(current_die)):
            print(f"{index + 1}. {current_die[index]}")

        print("6. Exit")

        index = int(input("\nWhich die do you want to remove? "))

        if MIN < index < MAX:
            current_die.pop(index - 1)
            if len(current_die) == MIN:
                dice_selection = False
        else:
            dice_selection = False

    return current_die


def re_roll(die: list) -> list:
    """ Repopulate list with die.

    After player has discarded die they don't want to keep, repopulates list with new dice rolls.

    :param die: current die the player has
    :return: full hand of dice
    """

    AMOUNT_OF_TIME_RE_ROLLED = 0
    MAX_TIMES_TO_RE_ROLL = 2

    while AMOUNT_OF_TIME_RE_ROLLED < MAX_TIMES_TO_RE_ROLL:
        remove_die(die)
        print("Your new hand is: ")
        print_current_hand(roll_die(die))
        print("\n")
        AMOUNT_OF_TIME_RE_ROLLED += 1

    return die


def take_turn():
    """
    Simulate single turn.
    """

    die = roll_die([])
    print_current_hand(die)

    roll_again = input("\nDo you want to re-roll any of the dice in your hand?\
                       \n\t1. Yes\n\t2. No\n")

    if roll_again == "1":
        re_roll(die)


def validate_singles(choice: int, die: str) -> int:
    """ Validate upper section.

    Checks if combo exists and returns the value of the combo.

    :param choice: which combo the player has selected
    :param die: current die the player has
    :precondition: choice is an int, die is a string
    :postcondition: returns an int of the value of the player's hand
    :return: value of player's combo as an int

    >>> validate_singles(1, '12345')
    1
    """

    if choice == 1 and re.search(r'[1]', die, re.I):
        return int(die.count('1'))
    elif choice == 2 and re.search(r'[2]', die, re.I):
        return int(die.count('2') * 2)
    elif choice == 3 and re.search(r'[3]', die, re.I):
        return int(die.count('3') * 3)
    elif choice == 4 and re.search(r'[4]', die, re.I):
        return int(die.count('4') * 4)
    elif choice == 5 and re.search(r'[5]', die, re.I):
        return int(die.count('5') * 5)
    elif choice == 6 and re.search(r'[6]', die, re.I):
        return int(die.count('6') * 6)
    else:
        return 0


def validate_three_of_a_kind(die):
    """ Validate three of a kind.

    Checks if combo exists and returns the value of the combo.

    :param die: current die the player has
    :precondition: die is a string
    :postcondition: returns an int of the value of the player's hand
    :return: value of player's combo as an int

    >>> validate_three_of_a_kind('23444')
    17
    """

    if re.search(r'([1-6])\1{2}', die, re.I):
        numbers = list(map(int, die))
        return sum(numbers)
    else:
        return 0


def validate_four_of_a_kind(die):
    """ Validate four of a kind.

    Checks if combo exists and returns the value of the combo.

    :param die: current die the player has
    :precondition: die is a string
    :postcondition: returns an int of the value of the player's hand
    :return: value of player's combo as an int

    >>> validate_four_of_a_kind('45555')
    24
    """

    if re.search(r'([1-6])\1{3}', die, re.I):
        numbers = list(map(int, die))
        return sum(numbers)
    else:
        return 0


def validate_full_house(die):
    """ Validate full house.

    Checks if combo exists and returns the value of the combo.

    :param die: current die the player has
    :precondition: die is a string
    :postcondition: returns an int of the value of the player's hand
    :return: value of player's combo as an int

    >>> validate_full_house('22255')
    25
    """

    if re.search(r'([1-6])\1{2}([1-6])\2', die, re.I):
        return 25
    elif re.search(r'([1-6])\1([1-6])\2{2}', die, re.I):
        return 25
    else:
        return 0


def validate_small_straight(die):
    """ Validate small straight.

    Checks if combo exists and returns the value of the combo.

    :param die: current die the player has
    :precondition: die is a string
    :postcondition: returns an int of the value of the player's hand
    :return: value of player's combo as an int

    >>> validate_small_straight('12345')
    30
    """

    remove_duplicates = list_to_string(sorted("".join(set(die))))
    if re.search(r'1234|2345|3456', remove_duplicates, re.I):
        return 30
    else:
        return 0


def validate_large_straight(die):
    """ Validate large straight.

    Checks if combo exists and returns the value of the combo.

    :param die: current die the player has
    :precondition: die is a string
    :postcondition: returns an int of the value of the player's hand
    :return: value of player's combo as an int

    >>> validate_large_straight('12345')
    40
    """

    if re.search(r'12345|23456', die, re.I):
        return 40
    else:
        return 0


def validate_yahtzee(die):
    """ Validate Yahtzee.

    Checks if combo exists and returns the value of the combo.

    :param die: current die the player has
    :precondition: die is a string
    :postcondition: returns an int of the value of the player's hand
    :return: value of player's combo as an int

    >>> validate_yahtzee('66666')
    50
    """

    if re.search(r'([1-6])\1{4}', die, re.I):
        return 50
    else:
        return 0


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

    #take_turn()


def main():
    """
    Drives the program
    """

    doctest.testmod(verbose=True)
    #initialize_game()


if __name__ == "__main__":
    main()
