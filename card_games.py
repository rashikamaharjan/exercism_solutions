"""Functions for tracking poker hands and assorted card tasks.
"""

def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    """
    return [number, number+1, number+2]

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.
    """

    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.
    """
    
    return number in rounds

def card_average(hand):
    """Calculate and returns the average card value from the list.
    """
    if 0 in hand:
        return sum(hand) / (len(hand)-1)
    else:
        return sum(hand)/len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.
    """
    
    return (hand[0]+hand[-1])//2 == card_average(hand) or hand[(len(hand)//2)+1] == card_average(hand)


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).
    """
    odd=[]
    even=[]
    for i in range(len(hand)):
        if i % 2 == 0:
            even.append(hand[i])
        else:
            odd.append(hand[i])
    return card_average(odd) == card_average(even)


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.
    """
    if hand[-1] == 11:
        hand[-1] = 22
    return hand

print(approx_average_is_average([0, 1, 5]))