import turtle
wn = turtle.Screen()
wn.bgcolor('skyblue')
x = turtle.Turtle()
y = turtle.Turtle()
z = turtle.Turtle()
def draw_housing():
    x.pensize(3)
    x.color('black', 'white')
    x.begin_fill()
    x.forward(80)
    x.left(90)
    x.forward(157)
    x.circle(40, 180)
    x.forward(157)
    x.left(90)
    x.end_fill()
draw_housing()
def circle(t, ht, colr):
    t.penup()
    t.forward(40)
    t.left(90)
    t.forward(ht)
    t.shape('circle')
    t.fillcolor(colr)
circle(x, 40, 'green')
circle(y, 100, 'orange')
circle(z, 160, 'red')
state_num = 0
def advance_state_machine():
    global state_num

    if state_num == 0:  
        z.color('darkgrey')
        y.color('darkgrey')
        x.color('green')
        wn.ontimer(advance_state_machine, 3000)
    elif state_num == 1:  
        z.color('darkgrey')
        y.color('orange')
        wn.ontimer(advance_state_machine, 1000)
        state_num = 2
    elif state_num == 2:  
        x.color('darkgrey')
        wn.ontimer(advance_state_machine, 1000)
        state_num = 3
    else:                
        z.color('red')
        y.color('darkgrey')
        wn.ontimer(advance_state_machine, 2000)
        state_num = 0
advance_state_machine()

wn.listen()

wn.mainloop()  
