from engine.bag import Bag, get_starting_chips

class Player:
    def __init__(self,
                 name,
                 has_potion=True
                 ):
        self.name = name
        self.victory_points = 0
        self.coins = 0
        self.rubies = 0
        self.has_potion = has_potion
        self.bag = Bag(chips=get_starting_chips())

    def add_victory_points(self, points):
        self.victory_points += points

    def __str__(self):
        return f"{self.name}: VC: {self.victory_points}"


if __name__ == "__main__":
    player = Player("Alice")
    print(player)

    