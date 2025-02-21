import random

MANDATORY_TOKENS = {
    'w1': 4,
    'w2': 2,
    'w3': 1,
    'g1': 1,
    'o1': 1,
}


class Token():
    def __init__(self, value, color):
        self.value = value
        self.color = color

        self.is_white = (color == 'white')  

        self._as_string = inv_color_map[self.color] + str(value)

    def __str__(self):
        return self._as_string        

class Bag():
    def __init__(self, bought_tokens={}):
    
        self._bag = []
    
        self.n_tokens = 0
        self.n_colored = 0

        # Init variables to keep track of all the white tokens
        self.white_tokens = {1: 0, 2:0 , 3:0}
        self.n_white = 0

        self._setup_bag(bought_tokens)


    def _setup_bag(self, bought_tokens={}):
        # Init an empty bag

        # First fill the bag with the starting tokens
        for key, val in MANDATORY_TOKENS.items():
            for _ in range(val):
                # Convert the string to token params
                color = color_map[key[0]]
                value = int(key[1])
                token = Token(color=color, value=value)
                self._bag.append(token)

                if color == 'white':
                    self.white_tokens[value] += 1

        for key, val in bought_tokens.items():
            for _ in range(val):
                # Convert the string to token params
                color = color_map[key[0]]
                value = int(key[1])
                token = Token(color=color, value=value)
                self._bag.append(token)

                if color == 'white':
                    self.white_tokens[value] += 1

    def sample(self):
        return random.sample(self._bag, 1)[0]

color_map = {
    'w': 'white',
    'o': 'orange',
    'g': 'green',
}

inv_color_map = {v: k for k, v in color_map.items()}
