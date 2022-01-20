import gzip
from flask import Flask
from models.response import Response
from datetime import date
from models.game import Game

app = Flask(__name__)

game_1 = Game("mario kart 8 deluxe", "nintendo", 2017, 44.49, 50000, False).json()
game_2 = Game("fortnite", "epic Games", 2017, 0.0, -1, False).json()
game_3 = Game("rocket league", "Psyonix", 2015, 31.66, 35000, False).json()

games_list = [game_3, game_1, game_2] # data

@app.route("/games")
def games():
    message = "You have {} game(s).".format(len(games_list))
    return Response(200, message, games_list).json()