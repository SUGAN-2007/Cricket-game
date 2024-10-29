import random
from join.over import s

player_scores=0
def batting():
    player_score=0
    for i in range(s):
        pc = random.randint(1,10)
        run=int(input('enter the number b/w 1 t0 10 : '))
        print(f'the bot number : {pc}')
        if run != pc and run <=10:
            player_score+=run
        else:
            print('you are out')
            break 
    global player_scores
    player_scores+=player_score
    print(f'the player score  : {player_score}')
