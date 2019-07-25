import turtle
turtle.bgcolor('purple')
turtle.shape('turtle')
finn=turtle.clone()
finn.shape('square')
finn.goto(100,0)
finn.goto(100,100)
finn.goto(0,100)
finn.goto(0,0)
charlie=turtle.clone()
charlie.shape('triangle')
charlie.left(90)
charlie.forward(100)
charlie.goto(50,150)
charlie.goto(100,100)
finn.penup()
finn.goto(-400,0)
finn.pendown()
finn.goto(-400,200)
finn.stamp()
finn.goto(-200,200)
finn.stamp()
finn.goto(-200,0)
finn.stamp()
finn.goto(-400,0)
finn.clearstamps()
ward=turtle.clone()
ward.penup()
ward.goto(350,0)
ward.pendown()
ward.pensize(5)
ward.color('yellow')
ward.left(90)
ward.forward(150)
ward.left(90)
ward.forward(75)
ward.color('white')
ward.left(90)
ward.forward(150)
gg=turtle.clone()
gg.penup()
gg.goto(350,0)
gg.pendown()
gg.color('green')
gg.pensize(10)
gg.right(90)
gg.forward(150)
gg.left(90)
gg.forward(75)
gg.color('blue')
gg.left(90)
gg.forward(150)
turtle.penup()
turtle.goto(0,-300)
turtle.pendown()


#Movement
def up():
    turtle.forward(10)
def down():
    turtle.back(10)
def right():
    turtle.right(45)        
def left():
    turtle.left(45)

turtle.onkeypress (up, "w")
turtle.onkeypress (down, "s")
turtle.onkeypress (right, "d")
turtle.onkeypress (left, "a")

turtle.pensize(20)
turtle.pencolor('red')



turtle.listen()
turtle.mainloop()





