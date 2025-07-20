n=[]
def over():
    ovesr=[1,2,5,10,20]
    o=int(input('number of overs (1,2,5,10,20):'))
    global n
    d=o*6
    n.append(d)
    if o in ovesr:
        print(f'you choose: {o} overs')
    
    else:
        print('choose correct overs')
        over()


