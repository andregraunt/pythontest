from turtle import *
fillcolor=['green', 'orange']
bgcolor('black')
width(2)
speed(9)

def zikl(a):
	for i in range(4):
		fd(a)
		lt(90)
		
a=100
for i in range(1000):
		color(fillcolor[i%2])
		begin_fill()
		zikl(a)
		a=a+2
		
		up()
		rt(188)
		bk(45)
		down()
end_fill()
 	

	
