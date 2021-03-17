import turtle
import time
wn = turtle.Screen()
wn.title ("Stoplights")
wn.bgcolor("black")
pen = turtle.Turtle()
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-30, 60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

red_light = turtle.Turtle()
red_light.shape("square")
red_light.color("#380000")
red_light.penup()
red_light.goto(0, 40)

yellow_light = turtle.Turtle()
yellow_light.shape("square")
yellow_light.color("#876100")
yellow_light.penup()
yellow_light.goto(0, 0)

green_light = turtle.Turtle()
green_light.shape("square")
green_light.color("#0f3923")
green_light.penup()
green_light.goto(0, -40)

while True:
    yellow_light.color("#876100")
    red_light.color("red")
    time.sleep(5)

    
    red_light.color("#380000")
    green_light.color("#47b300")
    time.sleep(7)

    green_light.color("#0f3923")
    yellow_light.color("yellow")
    time.sleep(3)

wn.mainloop()