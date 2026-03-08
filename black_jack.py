"""Functions to help play and score a game of blackjack.
"""


def value_of_card(card):
    """Determines the scoring value of a card.
    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card=='J' or card=='Q' or card=='K':
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determines which card has a higher value in the hand.
    """
    card1_val = value_of_card(card_one)
    card2_val = value_of_card(card_two)
    if card1_val == card2_val:
        return card_one, card_two
    elif card1_val > card2_val:
        return card_one
    else:
        return card_two


def value_of_ace(card_one, card_two):
    """Calculates the most advantageous value for an upcoming ace card.
    """

    card1_val = value_of_card(card_one)
    card2_val = value_of_card(card_two)
    if card1_val == 1 or card2_val == 1:
        return 1
    elif card1_val + card2_val <= 10:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    """Determines if the hand is a 'natural' or 'blackjack'.
    """

    card1_val = value_of_card(card_one)
    card2_val = value_of_card(card_two)
    if card1_val == 1 :
        card1_val = 11
    elif card2_val ==1:
        card2_val = 11
    if card1_val + card2_val == 21:
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.
    """
    card1_val = value_of_card(card_one)
    card2_val = value_of_card(card_two)
    if card1_val == card2_val:
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    """Determines if a blackjack player can place a double down bet.
    """

    card1_val = value_of_card(card_one)
    card2_val = value_of_card(card_two)
    if 9 <= card1_val+card2_val <= 11:
        return True
    else:
        return False