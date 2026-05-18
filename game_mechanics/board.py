NUM_TILES = 53

COINS = [*range(1, 16), 15, 16, 16, 17, 17, 18, 18, 19, 19, 20,
         20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27,
         27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 35]

VICTORY_POINTS = [
    0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3,
    3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8,
    8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12,
    12, 12, 13, 13, 13, 14, 14, 15]

RUBY = [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0,
        1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0]


class Square():
    def __init__(self, coins, victory_points, ruby):
        self.coins = coins
        self.victory_points = victory_points
        self.ruby = ruby


class Board():
    def __init__(self):
        self.squares = [Square(COINS[i], VICTORY_POINTS[i], RUBY[i])
                        for i in range(NUM_TILES)]
        self.droplet_default_position = 0
        

class Player():
    def __init__(
            self,
            color: str,
            droplet_position: int = 0,
            has_potion: bool = True,
            victory_points: int = 0,
            rubies: int = 0,
            bag_kwargs: dict = None,
            # brewing_policy: BrewingPolicy = None
            ):

        # Player state
        self.color = color
        self.droplet_position = droplet_position
        self.has_potion = has_potion
        self.victory_points = victory_points
        self.rubies = rubies

        # Init the default starting bag for the player
        # self.bag = Bag(**bag_kwargs)