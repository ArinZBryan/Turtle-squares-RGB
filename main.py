import turtle; import random
screen=turtle.Screen
Turtle=turtle.Turtle()
Turtle.shape("turtle")
Turtle.speed(0)
for j in range(90):
	Turtle.rt(4)
	r=random.randint(0,255)
	g=random.randint(0,255)
	b=random.randint(0,255)
	for i in range(4):
		Turtle.fd(100)
		Turtle.rt(90)
		Turtle.pencolor(r,g,b)




