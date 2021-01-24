from flask import render_template
from app import app
from app.models.game import *
from app.models.player import *




@app.route('/<player_1_choice>/<player_2_choice>', methods=['GET'])
def rock_paper_scissors(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    game = Game()
    
    return render_template("game.html", player_1=player_1, player_2=player_2)  
    