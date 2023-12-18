from random import randrange
from threading import*
import datetime
datetime.datetime.now()
print(datetime.datetime.now().date())
print(datetime.datetime.now().time())


print('Nathil :\n')

n= randrange(10)
def hello():
    print(f'mispar sodi {n}')

t = Timer(30.0, hello)
t.start()  

while True:

    V = int(input())
    if n== V:
        print(datetime.datetime.now().time())
        print( 'You win!')
        
        break  
    print(' Smaller' if (n< V) else'Bigger')


#def hello():
    #print(n)

#t = Timer(10.0, hello)
#t.start()  

