from turtle import Turtle, Screen

tom = Turtle()
tom.speed(8)

screen = Screen()
screen.title("Python Turtle Sheep")
screen.bgcolor("lightblue")

def draw_rectangle(x, y, width, height, color):
    tom.pu()
    tom.goto(x, y)
    tom.pd()
    tom.color(color)
    tom.begin_fill()

    tom.fd(width)
    tom.right(90)
    tom.fd(height)
    tom.right(90)
    tom.fd(width)
    tom.right(90)
    tom.fd(height)

    tom.end_fill()


def draw_tree(x, y):
    #tree_leaves
    tom.color("dark green")
    tom.pu()
    tom.goto(x, y)
    tom.pd()
    tom.begin_fill()
    tom.circle(25)
    tom.end_fill()

    #tree_trunk
    tom.pu()
    tom.fd(25 / 3)
    tom.pd()
    tom.right(90)
    tom.color("#654321")
    tom.begin_fill()

    tom.fd(30)
    tom.right(90)
    tom.fd(12.5)
    tom.right(90)
    tom.fd(30)
    tom.right(90)
    tom.fd(12.5)

    tom.end_fill()


def draw_circle(color, radius, x, y):
    tom.penup()
    tom.goto(x, y)
    tom.pendown()
    tom.color(color)
    tom.begin_fill()
    tom.circle(radius)
    tom.end_fill()


def draw_leg(x, y):
    tom.penup()
    tom.goto(x, y)
    tom.pendown()
    tom.color("black")
    tom.begin_fill()

    for _ in range(2):
        tom.forward(10)
        tom.right(90)
        tom.forward(35)
        tom.right(90)

    tom.end_fill()


def draw_sheep(legs, body, head, hair, ear, eyes):
    #legs
    for x, y in legs:
        draw_leg(x, y)

    #body
    for x, y in body:
        draw_circle("white", 25, x, y)

    #head
    x, y = head
    draw_circle("black", 20, x, y)

    #hair
    for x, y, radius in hair:
        draw_circle("white", radius, x, y)

    #ear
    tom.penup()
    tom.goto(ear)
    tom.pendown()
    tom.color("black")
    tom.begin_fill()
    tom.circle(6)
    tom.end_fill()

    #eyes
    for x, y in eyes:
        draw_circle("white", 4, x, y)
        draw_circle("black", 2, x - 1, y + 1)


#grass
draw_rectangle(-637, -100, 1290, 500, "green")

tom.pu()
tom.right(90)
tom.fd(500)
tom.pd()


#mountain1

tom.color("dark grey")
tom.begin_fill()

for i in range(3):
    tom.forward(400)
    tom.left(120)

tom.end_fill()

tom.left(60)

#snow1
tom.pu()
tom.color("white")
tom.begin_fill()
tom.fd(260)
tom.pd()
tom.fd(400 - 260)
tom.right(120)
tom.fd(170)
tom.right(90)
tom.fd(50)
tom.right(60)
tom.fd(50)
tom.left(60)
tom.fd(50)
tom.right(60)
tom.fd(48)
tom.right(90)
tom.fd(50)
tom.end_fill()


#mountain2

tom.pu()
tom.goto(-400, -100)
tom.right(60)
tom.pd()
tom.color("gray")
tom.begin_fill()

for i in range(3):
    tom.forward(350)
    tom.left(120)

tom.end_fill()

tom.left(60)

#snow2
tom.pu()
tom.color("white")
tom.begin_fill()
tom.fd(200)
tom.pd()
tom.fd(150)
tom.right(120)
tom.fd(140)
tom.right(140)
tom.fd(100)
tom.left(60)
tom.fd(72)
tom.left(180)
tom.fd(5)
tom.end_fill()


#mountain3

tom.pu()
tom.goto(150, -100)
tom.right(40)
tom.pd()
tom.color("gray")
tom.begin_fill()

for i in range(3):
    tom.forward(350)
    tom.left(120)

tom.end_fill()

tom.left(60)

#snow3
tom.pu()
tom.fd(250)
tom.color("white")
tom.begin_fill()
tom.pd()
tom.fd(100)
tom.right(120)
tom.fd(150)
tom.right(80)
tom.fd(50)
tom.right(100)
tom.fd(100)
tom.left(75)
tom.fd(38)
tom.right(100)
tom.right(35)
tom.fd(10)
tom.end_fill()


#sun
tom.pu()
tom.goto(-600, 210)
tom.right(60)
tom.pd()
tom.color("yellow")
tom.begin_fill()
tom.circle(150)
tom.end_fill()


#trees
draw_tree(105, -105)
draw_tree(-200, -200)
draw_tree(350, -160)
draw_tree(-400, -120)
draw_tree(-100, -100)
draw_tree(30, -260)


#sheep1

sheep1_legs = [
    (-30, -110),
    (-10, -110),
    (15, -110),
    (35, -110)
]

sheep1_body = [
    (-45, -105),
    (-25, -90),
    (0, -85),
    (25, -90),
    (45, -105),
    (30, -125),
    (0, -135),
    (-30, -125),
    (0, -105)
]

sheep1_head = (-45, -95)

sheep1_hair = [
    (-55, -65, 8),
    (-45, -60, 10),
    (-35, -65, 8)
]

sheep1_ear = (-30, -75)

sheep1_eyes = [
    (-51, -78),
    (-39, -78)
]

draw_sheep(
    sheep1_legs,
    sheep1_body,
    sheep1_head,
    sheep1_hair,
    sheep1_ear,
    sheep1_eyes
)


#sheep2

sheep2_legs = [
    (-485, -200),
    (-465, -200),
    (-440, -200),
    (-420, -200)
]

sheep2_body = [
    (-405, -195),
    (-425, -180),
    (-450, -175),
    (-475, -180),
    (-495, -195),
    (-480, -215),
    (-450, -225),
    (-420, -215),
    (-450, -195)
]

sheep2_head = (-405, -185)

sheep2_hair = [
    (-395, -155, 8),
    (-405, -150, 10),
    (-415, -155, 8)
]

sheep2_ear = (-420, -165)

sheep2_eyes = [
    (-411, -168),
    (-399, -168)
]

draw_sheep(
    sheep2_legs,
    sheep2_body,
    sheep2_head,
    sheep2_hair,
    sheep2_ear,
    sheep2_eyes
)

tom.hideturtle()
screen.mainloop()