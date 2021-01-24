from app.models.player import Player

class Game():
    def play(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        

def rock_paper_scissors(player_1, player_2, choice):
    if player_1_choice == "rock" and player_2_choice == "scissors":
        winner = player_1
    elif player_1_choice == "scissors" and player_2_choice == "rock":
        winner = player_2
    elif player_1_choice == "paper" and player_2_choice == "rock":
        winner = player_1
    elif player_1_choice == "rock" and player_2_choice == "paper":
        winner = player_1
    elif player_1_choice == "paper" and player_2_choice == "scissors":
        winner = player_2
    elif player_1_choice == "scissors" and player_2_choice == "paper":
        winner = player_1
    elif player_1_choice == player_2_choice:
        return None


