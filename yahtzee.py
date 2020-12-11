"""
Christine Le
A01235924
Final - Yahtzee
"""

import random
import re
import doctest

MIN = 0


def list_to_string(die: list) -> str:
    string = ""

    for item in sorted(die):
        string += str(item)

    return string


def return_key(choice):
    """ Take player input and return a key.

    Taking the player's input, returns the equivalent key to access the score in the player's score
    card.

    :param choice: int indicating player's choice
    :return: string that is a key

    >>> return_key(1)
    'Ones'
    """

    keys = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Three Of A Kind",
            "Four Of A Kind", "Full House", "Small Straight", "Large Straight", "Yahtzee",
            "Chance"]

    return keys[choice - 1]


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


def validate_three_of_a_kind(die: str) -> int:
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


def validate_four_of_a_kind(die: str) -> int:
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


def validate_full_house(die: str) -> int:
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


def validate_small_straight(die: str) -> int:
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


def validate_large_straight(die: str) -> int:
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


def validate_yahtzee(die: str) -> int:
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


def validate_chance(die: str) -> int:
    """ Validate chance.

    Returns the value of the combo.

    :param die: current die the player has
    :precondition: die is a string
    :postcondition: returns an int of the value of the player's hand
    :return: value of player's combo as an int

    >>> validate_chance('11335')
    13
    """

    numbers = list(map(int, die))
    return sum(numbers)


def combo_selection(choice: int, die: list) -> int:
    """ Check combo selection.

    Taking what combo choice the user has selected, checks to see if it is valid and if so, returns
    the value of the combo. If it is invalid, the user gets a 0.

    :param choice: int of what combo the player wants to choose
    :param die: list of dice the player currently has
    :precondition: list must contain integers from 1-6, combo choice must be a valid string
    :return: value of combo that player has selected

    >>> combo_selection(1, [1, 2, 3, 4, 5])
    1
    """

    die = list_to_string(die)

    if 0 < choice < 7:
        return validate_singles(choice, die)
    elif choice == 7:
        return validate_three_of_a_kind(die)
    elif choice == 8:
        return validate_four_of_a_kind(die)
    elif choice == 9:
        return validate_full_house(die)
    elif choice == 10:
        return validate_small_straight(die)
    elif choice == 11:
        return validate_large_straight(die)
    elif choice == 12:
        return validate_yahtzee(die)
    else:
        return validate_chance(die)


def update_score(player_card: dict, combo: str, combo_score: int, yahtzee_bonus: int) -> bool:
    """ Check if combo has been filled and updates if not.

    Checks player's score card to see if chosen combo is filled. If it is, prompt them to choose
    another one. If not, fill combo.

    :param player_card: dictionary containing player's scores
    :param combo: string that references which key to access in dictionary
    :param combo_score: int value of combo
    :param yahtzee_bonus: if Yahtzee is already filled and player gets another Yahtzee, add bonus
    :return: boolean if a score has been updated or not

    >>> update_score({"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,\
"Three Of A Kind": -1, "Four Of A Kind": -1, "Full House": -1, "Small Straight": -1, \
"Large Straight": -1, "Yahtzee": -1, "Chance": -1}, "Ones", 1, 0)
    True
    """
    for key, value in player_card.items():
        if combo == key:
            if combo == "Yahtzee" and value == 50:
                yahtzee_bonus += 50
            if value == -1:
                player_card[key] = combo_score
                return True


def combo_choice(card: dict, die: list, yahtzee_bonus: int):
    """ Prompt player for combo choice.

    Prints list of combos for player to choose from, then asks them which of the combos they would
    like to go with given their current hand.

    :param card: dictionary of player's scores and current existing combos
    :param die: list of player's current hand
    :param yahtzee_bonus: int indicating player's current Yahtzee bonus
    """

    print("\n")

    choices = ["1. Ones", "2. Twos", "3. Threes", "4. Fours", "5. Fives", "6. Sixes",
               "7. Three Of A Kind", "8. Four Of A Kind", "9. Full House", "10. Small Straight",
               "11. Large Straight", "12. Yahtzee", "13. Chance"]

    for option in choices:
        print(option)

    keep_looping = True

    while keep_looping:
        choice = int(input("\nWhich combo do you want to select for your hand? "))

        if update_score(card, return_key(choice), combo_selection(choice, die), yahtzee_bonus):
            return -1
        else:
            print("That combo is already filled.")


def check_upper_bonus(player_card: dict) -> bool:
    """ Check if player gets upper section bonus.

    Checks to see if sum of upper section is equal to or more than 63.

    :param player_card: dictionary containing player's scores
    :return: boolean if player qualifies for an upper section bonus

    >>> check_upper_bonus({"Ones": 1, "Twos": 2, "Threes": 3, "Fours": 4, "Fives": 5, "Sixes": 6,\
"Three Of A Kind": 17, "Four Of A Kind": 24, "Full House": 25, "Small Straight": 30, \
"Large Straight": 40, "Yahtzee": 50, "Chance": 10})
    False
    >>> check_upper_bonus({"Ones": 5, "Twos": 10, "Threes": 15, "Fours": 20, "Fives": 25,\
"Sixes": 30, "Three Of A Kind": 17, "Four Of A Kind": 24, "Full House": 25, "Small Straight": 30,\
"Large Straight": 40, "Yahtzee": 50, "Chance": 10})
    True
    >>> check_upper_bonus({"Ones": 4, "Twos": 2, "Threes": 3, "Fours": 4, "Fives": 20, "Sixes": 30,\
"Three Of A Kind": 17, "Four Of A Kind": 24, "Full House": 25, "Small Straight": 30,\
"Large Straight": 40, "Yahtzee": 50, "Chance": 10})
    True
    """

    upper_sum = player_card['Ones'] + player_card['Twos'] + player_card['Threes']
    upper_sum += player_card['Fours'] + player_card['Fives'] + player_card['Sixes']

    if upper_sum >= 63:
        return True
    else:
        return False


def calculate_score(player_card: dict) -> int:
    """ Calculate player's total score.

    Taking the dictionary containing the player's combos, sums up the total and applies a bonus if
    applicable.

    :param player_card: dictionary containing player's scores
    :return: int indicating player's total score

    >>> calculate_score({"Ones": 1, "Twos": 2, "Threes": 3, "Fours": 4, "Fives": 5, "Sixes": 6,\
"Three Of A Kind": 17, "Four Of A Kind": 24, "Full House": 25, "Small Straight": 30, \
"Large Straight": 40, "Yahtzee": 50, "Chance": 10})
    217
    >>> calculate_score({"Ones": 5, "Twos": 10, "Threes": 15, "Fours": 20, "Fives": 25,\
"Sixes": 30, "Three Of A Kind": 17, "Four Of A Kind": 24, "Full House": 25, "Small Straight": 30,\
"Large Straight": 40, "Yahtzee": 50, "Chance": 10})
    336
    """

    score = 0

    for value in player_card.values():
        score += value

    if check_upper_bonus(player_card):
        score += 35

    return score


def game_verdict(p1_score, p1_bonus, p2_score, p2_bonus):
    """ Decide game verdict.

    Decides who has won the game or if it is a tie.

    :param p1_score: int indicating player one's score
    :param p1_bonus: int indicating if player one has gotten more than one yahtzee
    :param p2_score: int indicating player two's score
    :param p2_bonus: int indicating if player two has gotten more than one yahtzee

    >>> game_verdict(200, 0, 201, 0)
    <BLANKLINE>
    <BLANKLINE>
    Player two is the winner with a score of 201 to 200!
    >>> game_verdict(150, 100, 200, 0)
    <BLANKLINE>
    <BLANKLINE>
    Player one is the winner with a score of 250 to 200!
    >>> game_verdict(300, 0, 300, 0)
    <BLANKLINE>
    <BLANKLINE>
    Both players got a score of: 300. The players tied!
    """

    p1_score += p1_bonus
    p2_score += p2_bonus

    print("\n")

    if p1_score == p2_score:
        print(f"Both players got a score of: {p1_score}. The players tied!")
    elif p1_score > p2_score:
        print(f"Player one is the winner with a score of {p1_score} to {p2_score}!")
    else:
        print(f"Player two is the winner with a score of {p2_score} to {p1_score}!")


def take_turn(player_card: dict, yahtzee_bonus: int):
    """ Simulate a single turn.

    Iterates through a single player's turn.

    :param player_card: dictionary containing player's score card
    :param yahtzee_bonus: int containing player's current Yahtzee bonus
    """

    die = roll_die([])
    print_current_hand(die)

    roll_again = input("\nDo you want to re-roll any of the dice in your hand?\
                       \n\t1. Yes\n\t2. No\n")

    if roll_again == "1":
        re_roll(die)

    combo_choice(player_card, die, yahtzee_bonus)
    print("-- PLAYER'S CURRENT SCORE --")
    print_score(player_card)


def initialize_game():
    """
    Print interface for players to start the game.
    """

    p1_card = create_score_card()
    p2_card = create_score_card()
    p1_bonus = MIN
    p2_bonus = MIN

    round_ongoing = True

    while round_ongoing:
        if -1 in p1_card.values():
            print("-- IT IS PLAYER ONE'S TURN --")
            take_turn(p1_card, p1_bonus)

        print("\n")

        if -1 in p2_card.values():
            print("-- IT IS PLAYER TWO'S TURN --")
            take_turn(p2_card, p2_bonus)

        if -1 not in p1_card.values() and -1 not in p2_card.values():
            round_ongoing = False

    game_verdict(calculate_score(p1_card), p1_bonus, calculate_score(p2_card), p2_bonus)


def main():
    """
    Drives the program
    """

    doctest.testmod(verbose=True)
    initialize_game()


if __name__ == "__main__":
    main()
