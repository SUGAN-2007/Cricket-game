import random
from join.bat import batting
from join.bowl import bowling
def decs(x,y):
    b=['batting','bowling']
    f=''.join(random.choices(b))
    b=['batting','bat']
    bo=['bowling','bowl'] 
    if x == y:
        d=input(' \n\nBATTING or BOWLING :').lower()      
        if d in b:
            print('')
            print('you choose to bat first') 
            batting() 
            print("\n\n your's bowling turn")
            bowling() 
        elif d in bo:
            print('')
            print('you choose to bowl first')
            bowling()
            print("\n\n your's batting turn")
            batting()
            
        else: 
            decs(x,y)   
    else:
        print(" ")
        print('bot choose to :',f)
        if f == 'batting':
            print('')
            print('bot choose to bat first')
            bowling() 
            print("\n\n your's batting turn")
            batting()
 
        else:
            print('')
            print('bot choose to bowl first') 
            batting()
            print("\n\n your's bowling turn")
            bowling()



