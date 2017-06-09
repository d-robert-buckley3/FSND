import turtle
from random import randint

def random_color():
    # return a random color compatible with turtle
    colors = [
        "blue",
        "red",
        "purple",
        "orange",
        "yellow",
        "brown",
        "white",
        "green",
        "cyan",
        "pink",
        "magenta"
        ]

    return colors[randint(0, len(colors) - 1)]

def draw_poly(sides, size, myturtle):
    # draw a polygon with variable size and sides
    
    for side in range(sides):
        myturtle.forward(size)
        myturtle.right(360/sides)

def draw_circle_of_polys(sides, size, resolution, myturtle):
    # repeat a poly, rotating slightly each time to end up
    # with a circle made of polys

    # To prevent an infinite loop, let's prevent a resolution < 1
    if resolution < 1:
        resolution = 1

    # we need to make our own turtle so it remains
    # constant throughout the drawing.

    for poly in range(360/resolution):
        draw_poly(sides, size, myturtle)
        myturtle.right(resolution)

def draw_flower(x, y):
    # draw a flower using a simple stem and a circle of polys
    # petal shape and color will be randomized
    petal_shape = randint(3, 8)

    for t in window.turtles():
        # Move turtle to mouseclick position
        t.penup()
        t.pencolor("green")
        t.fillcolor(random_color())
        t.setpos(x, y)

        # draw stem
        t.setheading(0)
        t.pendown()
        t.forward(200)

        # draw petals
        t.begin_fill()
        draw_circle_of_polys(petal_shape, 60, 15, t)
        t.end_fill()

        # draw center
        t.penup()
        t.setheading(90)
        t.forward(30)
        t.setheading(0)
        t.fillcolor("yellow")
        t.begin_fill()
        t.circle(30)
        t.end_fill()


def draw_initials(x, y):
    # draw my initials at current mouseclick position
    # pen color is randomized

    for t in window.turtles():
        # position pen and set color
        t.penup()
        t.goto(x, y)

        # save current position for reference
        current_pos = t.pos()

        t.pencolor(random_color())
        t.pendown()

        # draw first letter
        t.setheading(180)
        t.forward(50)
        t.circle(-20)

        # draw next letter
        t.penup()
        t.goto(current_pos)
        t.setheading(90)
        t.forward(20)
        t.setheading(180)
        t.forward(20)
        t.pencolor(random_color())
        t.pendown()
        t.forward(50)
        t.setheading(0)
        t.penup()
        t.forward(30)
        t.pendown()
        t.circle(-20, 90)

        # draw next letter
        t.penup()
        t.goto(current_pos)
        t.setheading(90)
        t.forward(60)
        t.setheading(180)
        t.pencolor(random_color())
        t.pendown()
        t.forward(50)
        t.circle(20)

        # draw last letter
        t.penup()
        t.goto(current_pos)
        t.setheading(90)
        t.forward(120)
        t.pencolor(random_color())
        t.pendown()
        t.circle(-10, 180)
        t.setheading(90)
        t.circle(-10, 180)
   

if __name__ == "__main__":
    window = turtle.Screen()
    window.bgcolor("gray")

    myturtle = turtle.Turtle()
    turtle.mode("logo")
    myturtle.shape("arrow")
    myturtle.speed(8)

    myturtle.write(
        "Click Anywhere!\nLeft click: flower\nRight click: initials", 
        move=True, 
        align="center", 
        font=("Arial", 24)
        )

    # set mouseclick bindings to drawing functions
    window.onclick(draw_flower, btn=1, add=True)
    window.onclick(draw_initials, btn=3, add=True)
    window.listen()

    # this sets the window to continue waiting for mouseclicks
    turtle.mainloop()

