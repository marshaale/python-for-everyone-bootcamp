class Player:
    game = "training"

    def __init__(self,username):
        self.username = username

player1 = Player("Messi")
player2 = Player("Ronaldo")

print(player1.username,player1.game)
print(player2.username,player2.game)