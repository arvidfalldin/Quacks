import numpy
from game_mechanics_file import Bag, Board


def probability_of_exploding(board: Board, bag: Bag):
    # If the current white score is below 5 then we cant explode
    current_white_score = board.white_score
    
    if current_white_score < 5:
        return 0

    n_tokens = len(bag)

    if current_white_score == 5:
        p = bag.n_white_geq[3] / n_tokens
    elif current_white_score == 6:
        p = bag.n_white_geq[2] / n_tokens
    else:
        p = bag.n_white_geq[1] / n_tokens
    return p
