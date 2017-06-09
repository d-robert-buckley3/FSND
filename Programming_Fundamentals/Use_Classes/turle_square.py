import turtle

def draw_square():
    num_sides = 4
    window = turtle.Screen()
    window.bgcolor("red")

    myturtle = turtle.Turtle()
    myturtle.shape("classic")
    myturtle.color("green")
    myturtle.speed(3)

    for side in range(num_sides):
        myturtle.forward(100)
        myturtle.right(90)

    window.exitonclick()


if __name__ == "__main__":
    draw_square()

    
