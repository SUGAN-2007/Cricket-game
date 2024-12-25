s = None
def over():
    ovesr=[1,2,5,10,20]
    o=+int(input('number of overs (1,2,5,10,20):'))
    global s
    n=o*6
    s=n
    if o in ovesr:
        print(f'you choose: {o} overs')
    
    else:
        print('choose correct overs')
        over()
sm=s

