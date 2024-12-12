#16.10.24
#Ülesanded 03

#Ülesanne 3.4 Lemmikraamat




















#Unistuste auto
mark, mudel = "bmw","118"
auto =" "+mudel
aasta = 1997
hind = 301.60

print("Minu unistuste auto on",auto,"aastas",aasta", mille hind on",hind,"eurot.")









#Ülesanne 3.6: Python Turtle kolmnurk
import turtle
kylje_pikkus = 100
nurk = 120
kujundi_varv = "red"

turtle.color(kujundi_varv)

for i in range(3):
    for i in range(3):
        turtle.forward(kylje_pikkus)
        turtle.left(nurk)

    turtle.penup()
    turtle.forward(kylje_pikkus*1,5)
    turtle.pendown()

turtle.done()
