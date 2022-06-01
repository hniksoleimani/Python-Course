import turtle

colors = ['black']
t = turtle.Pen('turtle')
t.speed(2)
turtle.bgcolor('white')
t.penup()
t.goto(50, 40)
t.pendown()

i = 0
while i <360:
    for j in range(len(colors)):
        t.pencolor(colors[j])
        t.width(i/100+1)
        t.forward(i)
        t.left(59)
        i += 1