from turtle import *
ser = 0
while ser <5:
	bgcolor('black')
	speed(9)
	color ("red")
	begin_fill()
	pensize(1)
	left (50)
	forward (130)
	circle(50,200)
	right (135)
	circle(50,200)
	forward (133)
	up()
	lt(23)
	fd(23)
	down()
	ser=ser+1
end_fill()
