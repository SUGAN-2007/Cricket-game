from join.bat import player_scores
from join.bowl import bot_scores
# def end():
if player_scores > bot_scores: 
    print("\n\nYou win the match")
else:
    print("\n\nYou lose the match")