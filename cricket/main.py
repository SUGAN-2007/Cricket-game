import random
from join.dec import decs
from join.over import over

c=over()
print("")

def tosss():
    coin=input('Head or Tail:').lower()
    toss=['head','tail']
    if coin in toss:
        f=''.join(toss)
        print (f,'wins')
        x=decs(coin,f)
    else:
        print("choose correct option")
        tosss()
tosss()