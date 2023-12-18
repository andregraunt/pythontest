from random import randrange

n= randrange(10)

while True:

    V = int(input())
    if n== V:
        print( 'You win!')

        break
    print(' Smaller' if (n< V) else'Bigger')
