class BasePolicy():
    def __init__(self):
        pass

    def rollout(self, bag):
        raise NotImplementedError

class GoBust():
    def __init__(self):
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

        return self.current_score, self.rollout