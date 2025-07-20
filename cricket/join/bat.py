import random
from join.over import n

player_scores=0
def batting():
    try:

        player_score=0
        for i in range(n[0]):
            pc = random.randint(1,6)
            run=int(input('enter the number b/w 1 t0 10 : '))
            print(f'the bot number : {pc}')
            if run != pc and run <=6:
                player_score+=run
            else:
                print('you are out')
                break 
        global player_scores
        player_scores+=player_score
        print(f'the player score  : {player_score}')
    except ValueError:
        print('enter the correct number')
        batting()