import turtle

def draw_poly(sides, size):
    window = turtle.Screen()
    window.bgcolor("white")

    myturtle = turtle.Turtle()
    myturtle.shape("classic")
    myturtle.color("black")
    myturtle.speed(2)

    for side in range(sides):
        myturtle.forward(size)
        myturtle.right(360/sides)

    window.exitonclick()

if __name__ == "__main__":
    draw_poly(3, 80)
