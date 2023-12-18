from turtle import*
from random import*
bgcolor('black')

speed(7)
up()
goto(-300, 0)
down()

pol=0
while pol==pol:
	w=randint(20, 80)
	a=randint(30, 600)

	width(w)
	color('#f515ff')
	forward(a)
	color('#feffea')
	back(a)
	
	pol=pol+1
	


while pol>=10:
	w=randint(20, 80)
	a=randint(30, 600)

	width(w)
	color('#ff1552')
	forward(a)
	color('#40ff82')
	back(a)
	
	pol=pol+1	
