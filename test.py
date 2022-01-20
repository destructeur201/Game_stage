from models.game import Game

game_1 = Game("mario kart 8 deluxe", "nintendo", 2017, 44.49, 50000, False)

game_2 = Game("fortnite", "epic Games", 2017, 0.0, -1, False)

game_3 = Game("rocket league", "Psyonix", 2015, 31.66, 35000, False)

print( game_1.json() )