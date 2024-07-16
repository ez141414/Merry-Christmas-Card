# 2022-11-28
# christmas_card.py
# Christmas Card
# Emma Zhang

# setup
import turtle
import random
import math
t = turtle
t.title("Merry Christmas Card")
t.setup(1000, 1000, 0, 0)
t.speed(-1)
t.pensize(0)

# sound

# colour vars
snowColour = "#FFFAFA"
pathColour = "#DEB887"
gingerBreadColour = "#C1844F"
lightGreen = "#6FECAA"
purple = "#6930AA"
green = "#3CB371"
blue = "#1634B9"
red = "#DC143C"
candyColours = [purple, green, blue, red]
starYellow = "#F4FF64"
treeBrown = "#6A4231"
sky = "#16304E"
gingerBreadBlue = "#5AC6F5"
moonYellow = "#FBFCD4"
moonOrSun = sky

# define functions
def penupdown(x, y) :
    t.penup()
    t.goto(x, y)
    t.pendown()

def rect(width, length, colour) :
    t.begin_fill()
    t.fillcolor(colour)
    t.pencolor(colour)
    for i in range(2) :
        t.forward(width)
        t.right(90)
        t.forward(length)
        t.right(90)
    t.end_fill()

def verticalOval(r, colour):
    t.begin_fill()
    t.fillcolor(colour)
    t.pencolor(colour)
    # t.left(45)
    for loop in range(2): 
        t.circle(r,90)  
        t.circle(r/2,90) 
    t.end_fill()

def horizontalOval(r, colour):
    t.begin_fill()
    t.fillcolor(colour)
    t.pencolor(colour)
    # t.right(45)
    for loop in range(2):
        t.circle(r,90)
        t.circle(r/2,90)
    t.end_fill()

def circle(r, colour) :
    t.begin_fill()
    t.fillcolor(colour)
    t.pencolor(colour)
    t.circle(r)
    t.end_fill()

def randCircle() :
    num = random.randint(1, 3)
    if num == 1 :
        lightColour = red
    elif num == 2 :
        lightColour = purple
    elif num == 3:
        lightColour = blue
    circle(4, lightColour)

def triangle(length, colour) :
    t.begin_fill()
    t.fillcolor(colour)
    t.pencolor(colour)
    t.setheading(315)
    t.forward(length/(math.sqrt(2)))
    t.right(45 + 90)
    t.forward(length)
    t.right(90 + 45)
    t.forward(length/(math.sqrt(2)))
    t.end_fill()

def light() :
    penupdown(320, 202)
    randCircle()
    penupdown(335, 223)
    randCircle()
    penupdown(332, 251)
    randCircle()

    penupdown(377, 257)
    randCircle()
    penupdown(381, 231)
    randCircle()
    penupdown(379, 207)
    randCircle()

    penupdown(450, 259)
    randCircle()
    penupdown(452, 242)
    randCircle()
    penupdown(466, 213)
    randCircle()


time = input("Night(N) or Day(D)") 
if time == "D" or time == "d" or time == "Day" or time == "day" :
    time = "D"
    sky = "#57C2DD"
    moonOrSun = moonYellow
else :
    time = "N"

# background
screen = turtle.Screen()
screen.bgcolor(sky)

# house
penupdown(-500, 230)
rect(260, 250, gingerBreadColour)
penupdown(-500, 230)
rect(265, 30, gingerBreadColour)

penupdown(-510, 231)
t.begin_fill()
t.fillcolor(gingerBreadColour)
t.pencolor(gingerBreadColour)
t.goto(-391, 371)
t.goto(-248, 231)
t.goto(-510, 231)
t.end_fill()

penupdown(-500, 230)
rect(235, 20, snowColour)
penupdown(-266, 210)
t.begin_fill()
t.fillcolor(snowColour)
t.circle(10)
t.end_fill()

# icing door frame
penupdown(-430, -17)
rect(86, -131, snowColour)
penupdown(-350 - 37, 114 - 38)
circle(43, snowColour)

# door 
penupdown(-415, -17)
rect(56, -126, gingerBreadColour)
penupdown(-350 - 37, 114 - 38 + 5)
circle(28, gingerBreadColour)
penupdown(-375, 61)
circle(9, snowColour)

# tree
t.setheading(0)
penupdown(377, 211)
rect(10, 25, treeBrown)
penupdown(380, 267)
triangle(35, green)
penupdown(380, 253)
triangle(50, green)
penupdown(380, 235)
triangle(65, green)

t.setheading(0)
penupdown(325, 203)
rect(10, 25, treeBrown)
penupdown(328, 260)
triangle(35, green)
penupdown(328, 246)
triangle(50, green)
penupdown(328, 228)
triangle(65, green)
penupdown(384, 266)
circle(6, starYellow)

t.setheading(0)
penupdown(446, 207)
rect(10, 25, treeBrown)
penupdown(451, 270)
triangle(35, green)
penupdown(451, 256)
triangle(50, green)
penupdown(451, 238)
triangle(65, green)

# snow ground
t.setheading(0)
penupdown(-500, -20)
t.begin_fill()
t.fillcolor(snowColour)
t.pencolor(snowColour)
for i in range(25) :
    t.forward(12)
    t.left(1.2)
for i in range(5) :
    t.forward(40)
    t.right(3.5)
for i in range(5) :
    t.forward(40)
    t.right(2)
for i in range(3) :
    t.forward(40)
    t.left(3)
for i in range(9) :
    t.forward(40)
    t.right(3)
t.goto(500, -500)
t.goto(-500, -500)
t.goto(-500, -20)
t.end_fill()

# house snow
t.setheading(50)
penupdown(-506, 238)
rect(180, 20, snowColour)
t.setheading(-44)
penupdown(-384, 372)
rect(190, 20, snowColour)
penupdown(-256, 222)
circle(10, snowColour)

# house candy
penupdown(-284, 249)
circle(10, candyColours[2])
penupdown(-314, 277)
circle(10, candyColours[3])
penupdown(-338, 300)
circle(10, candyColours[1])
penupdown(-363, 325)
circle(10, candyColours[2])

penupdown(-392, 350)
circle(10, candyColours[3])

penupdown(-415, 332)
circle(10, candyColours[1])
penupdown(-439, 304)
circle(10, candyColours[2])
penupdown(-462, 276)
circle(10, candyColours[3])
penupdown(-481, 253)
circle(10, candyColours[1])

# path
t.setheading(343)
penupdown(253, 168)
t.begin_fill()
t.fillcolor(pathColour)
t.pencolor(pathColour)
t.goto(253, 167)
t.goto(217, 165)
t.right(90)
for i in range(10) :
    t.forward(40)
    t.right(4)
for i in range(11) :
    t.forward(42)
    t.left(3)
t.goto(-290, -494)
penupdown(253, 168)
t.left(27)
for i in range(10) :
    t.forward(40)
    t.right(2)
for i in range(11) :
    t.forward(42)
    t.left(6)
t.goto(-290, -494)
t.end_fill()

# ginger bread man
penupdown(-25, 34)
circle(70, gingerBreadColour)
t.setheading(0)
penupdown(-16, 33)
rect(30, 30, gingerBreadColour)
t.setheading(350)
penupdown(-56, 20)
rect(100, 140, gingerBreadColour)

# left leg
penupdown(-78, -110)
t.setheading(340)
rect(50, 80, gingerBreadColour)
penupdown(-91, -164)
t.setheading(310)
rect(50, 80, gingerBreadColour)
penupdown(-120, -188)
t.setheading(310)
rect(50, 11, gingerBreadBlue)
penupdown(-141, -263)
t.setheading(0)
circle(25, gingerBreadColour)

# right leg
penupdown(-33, -128)
t.setheading(30)
rect(50, 150, gingerBreadColour)
penupdown(19, -218)
t.setheading(30)
rect(50, 11, gingerBreadBlue)
penupdown(64, -270)
t.setheading(0)
circle(25, gingerBreadColour)

# left arm
penupdown(-58, 20)
t.setheading(320)
rect(40, 140, gingerBreadColour)
penupdown(-133, -121)
t.setheading(0)
circle(20, gingerBreadColour)
penupdown(-128, -64)
t.setheading(320)
rect(40, 11, gingerBreadBlue)

# right arm
penupdown(7, -17)
t.setheading(30)
rect(40, 70, gingerBreadColour)
penupdown(41, -78)
t.setheading(40)
rect(40, 70, gingerBreadColour)
penupdown(99, -136)
t.setheading(0)
circle(20, gingerBreadColour)
penupdown(65, -107)
t.setheading(40)
rect(40, 11, gingerBreadBlue)

# eyes
penupdown(8, 87)
t.setheading(0)
circle(10, snowColour)
penupdown(55, 87)
t.setheading(0)
circle(9, snowColour)

# eyebrows
penupdown(-13, 125)
t.setheading(20)
rect(30, 11, gingerBreadBlue)
penupdown(51, 132)
t.setheading(340)
rect(25, 11, gingerBreadBlue)

t.hideturtle()

# mouth
penupdown(-15, 75)
t.pencolor(red)
t.setheading(310)
t.pensize(10)
for i in range(20) :
    t.forward(4)
    t.left(4)
t.pensize(0)
penupdown(-2, -38)
circle(10, red)
penupdown(-10, -85)
circle(10, red)

# moon
t.setheading(90)
penupdown(419, 377)
circle(23, moonYellow)
circle(15, moonOrSun)

# sleigh line
t.seth(35)
def polygon(n, length):
    angle = -0.2
    for i in range(n):
        t.forward(length)
        t.left(angle)

penupdown(-72, 270)
t.pencolor(gingerBreadColour)
n = 250
length = 100 / n
polygon(n, length)


# sleigh
penupdown(-124, 284)
t.seth(15)
rect(65, 41, red)
penupdown(-109, 288)
rect(50, 22, starYellow)
penupdown(-104, 295)
rect(50, 22, sky)
penupdown(-122, 277)
circle(4, red)

# santa
t.seth(0)
penupdown(-80, 279)
circle(7, pathColour)
t.begin_fill()
t.pencolor(red)
t.fillcolor(red)
penupdown(-89, 282)
t.goto(-77, 293)
t.goto(-92, 297)
t.goto(-89, 283)
t.end_fill()
penupdown(-96, 294)
circle(2, snowColour)
penupdown(-89, 283)
t.pensize(4)
t.goto(-79, 293)
t.pensize(0)

# reindeer body
penupdown(20, 287)
t.seth(-5)
rect(35, 15, gingerBreadColour)
penupdown(19, 285)

# tail
t.seth(-45)
rect(4, 15, gingerBreadColour)

# head
t.begin_fill()
t.fillcolor(gingerBreadColour)
penupdown(49, 286)
t.goto(53, 301)
t.goto(71, 294)
t.goto(49, 286)
t.end_fill()
t.seth(340)
penupdown(68, 292)
circle(2, red)

# neck
penupdown(51, 300)
rect(10, 20, gingerBreadColour)

# legs
t.seth(5)
penupdown(51, 300)
rect(6, 40, gingerBreadColour)
t.seth(-5)
penupdown(59, 260)
rect(-6, 8, gingerBreadColour)

t.seth(5)
penupdown(19, 286)
rect(6, 24, gingerBreadColour)
t.seth(-5)
penupdown(26, 262)
rect(-6, 8, gingerBreadColour)

# presents
t.seth(-5)
penupdown(-378, -90)
rect(100, 70, purple)
penupdown(-338, -94)
rect(18, 70, red)
penupdown(-334, -94)
circle(8, red)
penupdown(-324, -95)
circle(8, red)

t.seth(5)
penupdown(351, -5)
rect(60, 80, blue)
penupdown(373, -3)
rect(18, 80, starYellow)
penupdown(375, -3)
circle(10, starYellow)
penupdown(385, -2)
circle(10, starYellow)


# from and to
t.begin_fill()
t.fillcolor(snowColour)
t.pencolor(snowColour)
penupdown(80, 296)
t.goto(112, 309)
t.goto(112, 283)
t.goto(80, 296)
t.end_fill()

penupdown(127, 297)
name = input("Who is this card from?\n==> ")
t.write("From: " + str(name), font=("cookie", 18, "normal"))

penupdown(127, 269)
name = input("Who is this card to?\n==> ")
t.write("To: " + str(name), font=("cookie", 18, "normal"))


merryText = green
christmasText = green
# write text
if time == "D" :
    while True :
        penupdown(-210, 350)
        t.pencolor(merryText)
        t.write("MERRY", font=("cookie", 100, "normal"))
        if merryText == green :
            merryText = lightGreen
        else :
            merryText = green
        t.pencolor(merryText)
        penupdown(-220, 350)
        t.write("MERRY", font=("cookie", 100, "normal"))

        t.pencolor(christmasText)
        penupdown(-375, -475)
        t.write("CHRISTMAS", font=("cookie", 100, "normal"))
        if christmasText == green :
            christmasText = lightGreen
        else :
            christmasText = green
        t.pencolor(christmasText)
        penupdown(-385, -475)
        t.write("CHRISTMAS", font=("cookie", 100, "normal"))
        t.delay(100)
        screen.update()
else :
        penupdown(-210, 350)
        t.pencolor(lightGreen)
        t.write("MERRY", font=("cookie", 100, "normal"))
        penupdown(-220, 350)
        t.pencolor(green)
        t.write("MERRY", font=("cookie", 100, "normal"))
        penupdown(-375, -475)
        t.pencolor(lightGreen)
        t.write("CHRISTMAS", font=("cookie", 100, "normal"))
        penupdown(-385, -475)
        t.pencolor(green)
        t.write("CHRISTMAS", font=("cookie", 100, "normal"))


# tree lights
if time == "N" :
    while True :
        light()
        t.delay(10)
        screen.update()
else :
    light() 

t.exitonclick()

# def buttonclick(x,y):
#     print("You clicked at ({0},{1})".format(x,y))
# t.onscreenclick(buttonclick, 1)

t.done()