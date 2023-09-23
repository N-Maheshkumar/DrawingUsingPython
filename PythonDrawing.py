from sketchpy import canvas
import turtle
obj = canvas.sketch_from_svg("bablu.svg")
t=turtle.Turtle()
t.penup()
t.goto(-60,-290)
t.pendown()
t.pencolor("#008000")
t.write("Happy Bablu Day",align="center", font=("Arial",40,"bold"))
obj.draw()
t.hideturtle()
turtle.done()