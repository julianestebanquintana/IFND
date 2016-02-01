import turtle

window = turtle.Screen()
window.bgcolor("white")
brad = turtle.Turtle()
i = 0
while i < 36:
	y = 0
	while y < 3:
		brad.forward(100)
		brad.right(56.6)
		y += 1
	brad.right(10)
	i += 1

window.exitonclick()
