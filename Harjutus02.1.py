# Darion Pukk 08.10.24
# Harjutus 02.1
# Olümpiarõngad

import turtle
aken = turtle.Screen()
aken.setup(width=500, height=400)
aken.title("Olümpiarõngad - Darion")
turtle.speed(0)
turtle.pensize(6)


#sinine
turtle.penup()
turtle.goto(-110,30)
turtle.pendown()
turtle.pencolor("blue")
turtle.circle(50)


#must
turtle.penup()
turtle.goto(-0,30)
turtle.pendown()
turtle.pencolor("black")
turtle.circle(50)



#punane
turtle.penup()
turtle.goto(110,30)
turtle.pendown()
turtle.pencolor("red")
turtle.circle(50)



#kollane
turtle.penup()
turtle.goto(-55,-20)
turtle.pendown()
turtle.pencolor("yellow")
turtle.circle(50)



#kollane
turtle.penup()
turtle.goto(55,-20)
turtle.pendown()
turtle.pencolor("green")
turtle.circle(50)





turtle.done()