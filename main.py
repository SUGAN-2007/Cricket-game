import random
from join.dec import decs
from join.over import over

c=over()
print("")
coin=input('Head or Tail:').lower()
toss=['head','tail']
tosse=random.choices(toss)    
if coin in toss:
    f=''.join(tosse)
    print (f,'wins')
    x=decs(coin,f)
else:
    print("you are disqualified")