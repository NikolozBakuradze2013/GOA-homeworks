from turtle import *

#we want to paint a house

#step 1: draw a square
speed(5)
width(7)
color("yellow")
begin_fill()
forward(200) 
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("brown")
begin_fill()
left(90)
forward(90)
right(90)
forward(60)
right(90)
forward(90) 
end_fill() #height of the door

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("blue")
begin_fill()
left(30)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)

penup()
goto(200, 200)
pendown()

left(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
end_fill()
exitonclick()