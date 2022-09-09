class Game:

    player: Player()

    def __init__(self, player):
        self.player = player


game = Game(Player())
