#By: TheSpikyHedgehog
import turtle

def midpoint(p1, p2):
    x_midpoint = (p1[0] + p2[0]) / 2
    y_midpoint = (p1[1] + p2[1]) / 2
    return (x_midpoint, y_midpoint)
def draw_triangle(points, color):
    turtle.penup()
    turtle.goto(points[0][0], points[0][1])
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.goto(points[1][0], points[1][1])
    turtle.goto(points[2][0], points[2][1])
    turtle.goto(points[0][0], points[0][1])
    turtle.end_fill()
def sierpinski(points, depth):
    color = ["Plum1", "DarkSeaGreen1", "SlateGray1"]
    draw_triangle(points, color[depth % 3])
    if depth > 0:
        sierpinski([points[0], midpoint(points[0], points[1]), midpoint(points[0], points[2])], depth-1)
        sierpinski([points[1], midpoint(points[0], points[1]), midpoint(points[1], points[2])], depth-1)
        sierpinski([points[2], midpoint(points[2], points[1]), midpoint(points[0], points[2])], depth-1)


def main():
    turtle.speed(1000)
    turtle.hideturtle()
    turtle.title("Sierpinski Triangle.")
    # depth = input("How many recursions?")
    depth = int(turtle.numinput(title="depth",prompt="How many times do you want to do the recursion?>"))
    points = [(-200, -100), (0, 200), (200, -100)]
    
    sierpinski(points, depth)

    turtle.mainloop()

main()