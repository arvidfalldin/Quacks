from game_mechanics_file import Bag, Board

class QuacksEnvironment():
    def __init__(self):
        self._board = None
        self._bag = None

    def step(self, action):
        """
        Play a token and return resulting state
        (Bag, Board)
        """

        if action == 1:
            # Draw a token from the bag
            token = self._bag.sample()

            # Play the token and observe outcome
            self._board.play_token(token)
        elif action == 2:
            self._board.potion_available = False
            token = self._board.remove_last_token()
            self._bag.add(token)

        return self._board, self._bag


    def reset(self, board, bag):
        """
        Reset the environment with a fresh bag and board
        """
        self._board = board
        self._bag = bag

