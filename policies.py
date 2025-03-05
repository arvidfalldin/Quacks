import sys
import inspect


class BasePolicy():
    def __init__(self):
        pass

    def rollout(self, bag):
        raise NotImplementedError

    def reset(self,):
        raise NotImplementedError

class GoBust(BasePolicy):
    def __init__(self, *args, **kwargs):
        self.reset()

    def reset(self):
        self.white_score = 0
        self.current_score = 0
        self.rollout = []

    def play(self, bag):
        multiplier = 1
        while self.white_score < 8:
            token = bag.sample()
            if token.is_white:
                self.white_score += token.value
            self.current_score += token.value*multiplier
            self.rollout.append(token)

            if token.color == 'yellow':
                multiplier = 2
            else:
                multiplier = 1

        # With this policy we always play until we explode
        exploded = True

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