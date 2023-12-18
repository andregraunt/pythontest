from random import randrange
from threading import*

n= randrange(10000)
def hello():
    print(f'mispar sodi {n}')

t = Timer(10.0, hello)
t.start()  

while True:

    V = int(input())
    if n== V:
        print( 'You win!')

        break
    print(' Smaller' if (n< V) else'Bigger')


#def hello():
  #  print(n)

#t = Timer(10.0, hello)
#t.start()  

