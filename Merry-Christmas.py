                                        # INSTAGRAM @pcmuhendisii

from turtle import *
from random import randint

def create_triangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()

    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)

    turtle.end_fill()
    turtle.setheading(0)

def create_circle(turtle, x, y, radius, color):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_tree(turtle, x, y):
    """Draws a tree at the specified coordinates."""
    create_triangle(turtle, "#855E42", x - 15, y - 60, 30, 60)  # Trunk
    width = 240
    while width > 10:
        width -= 10
        height = 10
        x_center = x - width / 2
        create_triangle(turtle, "green", x_center, y, width, height)  # Tree leaves
        y += height
    turtle.penup()
    turtle.color('yellow')
    turtle.goto(x - 20, y + 10)  # Top of the star
    turtle.begin_fill()
    turtle.pendown()
    for _ in range(5):
        turtle.forward(40)
        turtle.right(144)
    turtle.end_fill()

def draw_clouds(turtle, x, y):
    """Draws a cloud."""
    create_circle(turtle, x - 25, y, 30, "#d3d3d3")
    create_circle(turtle, x + 25, y, 30, "#d3d3d3")
    create_circle(turtle, x, y + 20, 40, "#d3d3d3")
    create_circle(turtle, x - 35, y + 10, 30, "#d3d3d3")
    create_circle(turtle, x + 35, y + 10, 30, "#d3d3d3")

# Screen setup
SKY_COLOR = "#191970"  # Sky color (blue)
GROUND_COLOR = "brown"  # Ground color (brown)

pcmuh = Turtle()
pcmuh.speed(0)  # Fast mode
screen = pcmuh.getscreen()

screen.title("Pcmuhendisii")
screen.setup(width=1.0, height=1.0)

# Split the background into two colors
screen.bgcolor(SKY_COLOR)  # Fill the sky
pcmuh.penup()
pcmuh.goto(-screen.window_width()//2, -screen.window_height()//2)  # Move to bottom-left
pcmuh.pendown()
pcmuh.color(GROUND_COLOR)
pcmuh.fillcolor(GROUND_COLOR)
pcmuh.begin_fill()
pcmuh.goto(screen.window_width()//2, -screen.window_height()//2)  # Bottom-right
pcmuh.goto(screen.window_width()//2, 0)  # Right-middle
pcmuh.goto(-screen.window_width()//2, 0)  # Left-middle
pcmuh.goto(-screen.window_width()//2, -screen.window_height()//2)  # Bottom-left
pcmuh.end_fill()

# Place clouds at the top (with equal spacing between them)
clouds_x_positions = [-screen.window_width()//2 + 70, -screen.window_width()//6, screen.window_width()//6, screen.window_width()//2 - 70]

for x in clouds_x_positions:
    draw_clouds(pcmuh, x, screen.window_height()//2 - 50)

# Randomly generate stars
number_of_stars = randint(20, 30)
for _ in range(0, number_of_stars):
    x_star = randint(-(screen.window_width()//2), screen.window_width()//2)
    y_star = randint(0, screen.window_height()//2)
    size = randint(5, 20)
    pcmuh.penup()
    pcmuh.color('white')
    pcmuh.goto(x_star, y_star)
    pcmuh.begin_fill()
    pcmuh.pendown()
    for _ in range(5):
        pcmuh.forward(size)
        pcmuh.right(144)
    pcmuh.end_fill()

# Snow effect on the ground
for _ in range(45):  # 45 random snowflakes
    x_snow = randint(-screen.window_width()//2, screen.window_width()//2)
    y_snow = randint(-screen.window_height()//2, 0)
    create_circle(pcmuh, x_snow, y_snow, 3, "white")

# Snow and stars
pcmuh.speed(100)
create_circle(pcmuh, 230, 180, 60, "white")
create_circle(pcmuh, 220, 180, 60, SKY_COLOR)

# Draw trees
draw_tree(pcmuh, -200, -200)  # Left tree (moved down)
draw_tree(pcmuh, 200, -200)   # Right tree (moved down)
draw_tree(pcmuh, 0, -100)     # Middle tree

# Display messages
pcmuh.speed(1)
pcmuh.penup()
msg = "Happy Christmas Day"
pcmuh.goto(0, -300)
pcmuh.color("#00FFFF")
pcmuh.pendown()
pcmuh.write(msg, move=False, align="center", font=("Aharoni", 15, "bold"))

pcmuh.speed(1)
pcmuh.penup()
msg = "ig: @pcmuhendisii"
pcmuh.goto(60, -330)
pcmuh.color("white")
pcmuh.pendown()
pcmuh.write(msg, move=False, align="center", font=("Arial", 10, 'italic'))

pcmuh.hideturtle()
screen.mainloop()