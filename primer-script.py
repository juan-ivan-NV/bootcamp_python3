import turtle

turtle.setup(900, 800)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title(' Hello World !')

tess = turtle.Turtle()
tess.shape("turtle")
tess.color("red")


tess.penup()
size = 20
for i in range(50):
    tess.stamp()
    size = size + 3
    tess.forward(size)
    tess.right(24)

wn.exitonclick()
