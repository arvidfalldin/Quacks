import numpy
from game_mechanics import Bag, Token


def probability_of_exploding(bag: Bag, current_white_score):
    # If the current white score is below 5 then we cant explode
    if current_white_score < 5:
        return 0

    n_tokens = len(bag)

    if current_white_score == 5:
        p = bag.white_tokens[3] / n_tokens
    elif current_white_score == 6:
        p = (bag.white_tokens[3] + bag.white_tokens[2]) / n_tokens
    else:
        p = (bag.white_tokens[3]
             + bag.white_tokens[2]
             + bag.white_tokens[1]) / n_tokens
    return p
