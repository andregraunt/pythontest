from turtle import*


left (90)
color('red')
width(2)
bgcolor('black')

speed (0)
#recursion
def draw(l):
    if (l<10):
        return
    else:
        forward(l)
        left(30)
        draw(3*l/4)
        right(60)
        draw(3*l/4)
        left(30)
        backward(l)
  
#k=0
#while k==10:  
draw(80)
	
