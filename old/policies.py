import sys
import inspect
from policy_utils import probability_of_exploding

class BasePolicy():
    def __init__(self):
        pass

    def __call__(self, board, bag):
        raise NotImplementedError

    def reset(self,):
        raise NotImplementedError


class GoBust(BasePolicy):
    """
    Play and keep playing until we explode
    """
    def __init__(self, *args, **kwargs):
        self.reset()

    def reset(self):
        pass

    def __call__(self, *args, **kwargs):
        """
        Always return True i.e. keep playing
        """
        return True


class ProbOfExploding():
    def __init__(self, p_stop=1.0, *args, **kwargs):
        self.reset()
        self.p_stop = p_stop

    def reset(self):
        pass


    def __call__(self, board, bag):

        if board.potion_available:
            last_token = board[-1]
            if last_token.color == 'white' and last_token.value == 3:
                return 2

        # Check the probability of exploding on the next move
        p_explode = probability_of_exploding(board, bag)

        # If above threshold, end the round, else play
        if p_explode > self.p_stop:
            return 0
        else:
            return 1



class ProbabilityOfExploding():

    def __init__(self, p_stop=0.25, *args, **kwargs):
        self.reset()
        self.p_stop = p_stop

    def reset(self):
        self.white_score = 0
        self.current_score = 0
        self.rollout = []

    def play(self, bag):
        multiplier = 1
        exploded = False
        stop = False
        p_fail = 0

        while not stop:
            token = bag.sample()
            if token.is_white:
                self.white_score += token.value
            self.current_score += token.value * multiplier
            self.rollout.append(token)

            if token.color == 'yellow':
                multiplier = 2
            else:
                multiplier = 1

            if (self.white_score > 7):
                exploded = True
            else:
                p_fail = probability_of_exploding(
                bag=bag,
                current_white_score=self.white_score)
            
            if exploded or p_fail > self.p_stop:
                stop = True

        # Collect the outcome in a dict
        outcome = {
            'score': self.current_score,
            'exploded': exploded,
            'rollout': self.rollout,
        }

        self.reset()

        return outcome


clsmembers_pairs = inspect.getmembers(sys.modules[__name__], inspect.isclass)
POLICYS = {k: v for (k, v) in clsmembers_pairs}