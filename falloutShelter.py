#fallout shelter logo in Python
from turtle import *

speed(0)
bgcolor("gold")

# Black circle
penup()
goto(0, -225)
pendown()
color("black")
begin_fill()
circle(225)
end_fill()

# Triangles
penup()
goto(0, 0)
pendown()
color("gold")
begin_fill()
for i in range(3):
    right(120)
    for i in range(3):
        forward(200)
        right(120)
end_fill()

hideturtle()
