import random
from join.over import n

bot_scores=0
def bowling():
    try:
        bot_score=0
        for i in range(n[0]):
            pc = random.randint(1,6)
            print('the bot number : **')
            run=int(input('enter the number b/w 1 t0 6 : '))
            if run != pc and run <=6:
                print(f'the bot number : {pc}') 
                bot_score+=run
            else:
                print('bot is out')
                break 
        global bot_scores
        bot_scores+=bot_score
        print(f'the bot score : {bot_score}')
    except ValueError:
        print('enter the correct number')
        bowling()

