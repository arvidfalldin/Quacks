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
        self.is_yellow = (color == 'yellow')

        self._as_string = INV_COLOR_MAP[self.color] + str(value)

    def __str__(self):
        return self._as_string

    def __eq__(self, token):
        return (self.value == token.value and self.color == token.color)


class Bag():
    def __init__(self, bought_tokens={}, *args, **kwargs):
        self._bag = []

        self.n_tokens = 0

        # Init variables to keep track of all the white tokens

        # Num token of value greater than or equal
        self.n_white_geq = {1: 0, 2: 0, 3: 0}
       
        self._setup_bag(bought_tokens)

    def _setup_bag(self, bought_tokens={}):
        """
        Setup a new bag. Note, this should only be called
        at init. If we want to add things to the bag at any other
        point --- use the <add> method
       """

        # First fill the bag with the starting tokens
        for key, val in MANDATORY_TOKENS.items():
            for _ in range(val):
                # Convert the string to token params
                color = COLOR_MAP[key[0]]
                value = int(key[1])
                token = Token(color=color, value=value)

                # Add the token to the bag
                self._add_token(token)

        # Also add any bought tokens
        for key, val in bought_tokens.items():
            for _ in range(val):
                # Convert the string to token params
                color = COLOR_MAP[key[0]]
                value = int(key[1])
                token = Token(color=color, value=value)

                # Add the token to the bag
                self._add_token(token)
    
    def add(self, input):
        """
        Add token or list of tokens to the bag
        """
        if isinstance(input, Token):
            # Add token to bag
            self._add_token(input)

        elif isinstance(input, list):
            for token in input:
                # Add token to bag
                self._add_token(token)

    def _add_token(self, token):
        """
        Add a token to the bag
        """
        self._bag.append(token)

        # If white, note its value and add to geq-dict
        # for fast prob. of explosion computation
        if token.is_white:
            self.n_white_geq[1] += 1
            if token.value == 2:
                self.n_white_geq[2] += 1
            elif token.value == 3:
                self.n_white_geq[2] += 1
                self.n_white_geq[3] += 1

    def _remove_token(self, token):
        """
        Remove a token from the bag
        """
        self._bag.remove(token)

        # If white, note its value and update the geq-dict
        # for fast prob. of explosion computation
        if token.is_white:
            self.n_white_geq[1] += -1
            if token.value == 2:
                self.n_white_geq[2] += -1
            elif token.value == 3:
                self.n_white_geq[2] += -1
                self.n_white_geq[3] += -1

    def __str__(self):
        """
        Format bag
        """
        s = '('
        for token in self._bag:
            s += str(token) + ', '
        return s[:-2] + ')'

    def __len__(self):
        """
        Return number of tokens in bag
        """
        return len(self._bag)

    def sample(self):
        sample = random.sample(self._bag, 1)[0]

        # Remove token from bag and update stats
        self._remove_token(sample)
        # if sample.color == 'white':
        #     self.white_tokens[sample.value] += -1
        #     self.n_white += 1
        return sample

    # def reset(self):
    #     # NOTE Not sure if .copy() is necessary here..
    #     self._bag = self._bag_backup.copy()

    #     self.white_tokens = {1: 0, 2: 0, 3: 0}
    #     self.n_white = 0
    #     for token in self._bag:
    #         if token.color == 'white':
    #             self.n_white += 1
    #             self.white_tokens[token.value] += 1


class Board():
    def __init__(self, rat_position=0, potion_available=True):
        # Start out with an empty sequence of tokens
        self._tokens = []
        self.rat_position = rat_position
        self.potion_available = potion_available

        # List of rewards for each slot on the board
        self.coins = COINS
        self.victory_points = VICTORY_POINTS
        self.ruby = RUBY

        # Some short-hand variables describing the state 
        self.white_score = 0
        self.has_exploded = 0
        self.current_pos = 0
        self.step_mult = 1

    def play_token(self, token):
        """
        Add a token to the board
        """
        self._tokens.append(token)
        self.current_pos += token.value * self.step_mult

        # white tokens bring us closer to exploding
        if token.is_white:
            self.white_score += token.value
            # If white score is 8 or more we have exploded
            self.has_exploded = (self.white_score > 7)

        # If a token is yellow the next token's
        # value is multiplied with 2
        if token.is_yellow:
            self.step_mult = 2
        else:
            self.step_mult = 1

    def remove_last_token(self):
        token = self._tokens.pop()
        self.current_pos += -1 * token.value * self.step_mult

        # If the tokn was white remove its effects
        if token.is_white:
            self.white_score += -token.value

        return token

    def __getitem__(self, index):
        return self._tokens[index]

    def empty(self):
        """
        clear the board and return a list of the
        tokens from the played round to be returned
        to the bag
        """
        played_tokens = self._tokens
        self._tokens = []
        return played_tokens

    def __str__(self):
        if len(self._tokens) == 0:
            return '()'

        s = '('
        for token in self._tokens:
            s += str(token) + ', '
        return s[:-2] + ')'


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