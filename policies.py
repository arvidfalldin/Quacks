import sys
import inspect


class BasePolicy():
    def __init__(self):
        pass

    def rollout(self, bag):
        raise NotImplementedError


class GoBust():
    def __init__(self, *args, **kwargs):
        self.white_score = 0
        self.current_score = 0
        self.rollout = []

    def play(self, bag):
        while self.white_score < 8:
            token = bag.sample()
            if token.is_white:
                self.white_score += token.value
            self.current_score += token.value
            self.rollout.append(token)

        # With this policy we always play until we explode
        exploded = True

        # Collect the outcome in a dict
        outcome = {
            'score': self.current_score,
            'exploded': exploded,
            'rollout': self.rollout,
        }

        return outcome


clsmembers_pairs = inspect.getmembers(sys.modules[__name__], inspect.isclass)
POLICYS = {k: v for (k, v) in clsmembers_pairs}