import random

MANDATORY_TOKENS = {
    'w1': 4,
    'w2': 2,
    'w3': 1,
    'g1': 1,
    'o1': 1,
}

COLOR_MAP = {
    'w': 'white',
    'o': 'orange',
    'g': 'green',
    'k': 'black',
    'y': 'yellow',
}

INV_COLOR_MAP = {v: k for k, v in COLOR_MAP.items()}


class Token():
    def __init__(self, value, color):
        self.value = value
        self.color = color

        self.is_white = (color == 'white')

        self._as_string = INV_COLOR_MAP[self.color] + str(value)

    def __str__(self):
        return self._as_string

    def __eq__(self, token):
        return (self.value == token.value and self.color == token.color)


class Bag():
    def __init__(self, bought_tokens={}, *args, **kwargs):

        self._bag = []
        self._bag_backup = []

        self.n_tokens = 0
        self.n_colored = 0

        # Init variables to keep track of all the white tokens
        self.white_tokens = {1: 0, 2: 0, 3: 0}
        self.n_white = 0

        self._setup_bag(bought_tokens)

    def _setup_bag(self, bought_tokens={}):
        # Init an empty bag

        # First fill the bag with the starting tokens
        for key, val in MANDATORY_TOKENS.items():
            for _ in range(val):
                # Convert the string to token params
                color = COLOR_MAP[key[0]]
                value = int(key[1])
                token = Token(color=color, value=value)
                self._bag.append(token)

                if color == 'white':
                    self.white_tokens[value] += 1

        for key, val in bought_tokens.items():
            for _ in range(val):
                # Convert the string to token params
                color = COLOR_MAP[key[0]]
                value = int(key[1])
                token = Token(color=color, value=value)
                self._bag.append(token)

                if color == 'white':
                    self.white_tokens[value] += 1

        # Make a copy of the original bag for easy resetting
        self._bag_backup = self._bag.copy()

    def add_token(self, token):
        # TODO Ugly, Fix this
        self._bag_backup.append(token)

    def __str__(self):
        s = '('
        for token in self._bag:
            s += str(token) + ', '
        return s[:-2] + ')'

    def __len__(self):
        return len(self._bag)

    def sample(self):
        sample = random.sample(self._bag, 1)[0]
        self._bag.remove(sample)
        if sample.color == 'white':
            self.white_tokens[sample.value] += -1
            self.n_white += 1
        return sample

    def reset(self):
        # NOTE Not sure if .copy() is necessary here..
        self._bag = self._bag_backup.copy()

        self.white_tokens = {1: 0, 2: 0, 3: 0}
        self.n_white = 0
        for token in self._bag:
            if token.color == 'white':
                self.n_white += 1
                self.white_tokens[token.value] += 1


class Board():
    def __init__(self, rat_position=0, potion_available=True):
        # Start out with an empty sequence of tokens
        self._tokens = []
        self.rat_position = rat_position
        self.potion_available = potion_available



# Data on the rewards associated with each slot on the board
COINS = [*range(1, 16), 15, 16, 16, 17, 17, 18, 18, 19, 19, 20,
         20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27,
         27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 35]

VICTORY_POINTS = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3,
                  3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8,
                  8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12,
                  12, 12, 13, 13, 13, 14, 14, 15]

RUBY = [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0,
        1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0]