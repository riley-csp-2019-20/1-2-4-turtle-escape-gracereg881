import turtle as trtl
import random 

# import the turtle
drawbot = trtl.Turtle()
drawbot.ht()
drawbot.speed(0)
drawbot.color("darkblue")

player = trtl.Turtle()
player.turtlesize(2)
player.color("lightblue")
player.pencolor("turquoise")
player.up()
player.goto(-60,50)



# setting variables and amounts for multiple things
amount = 40
wall_width = 20
drawbot.pensize(4)
door_width = 35
barrier_length = 37

def up():
    player.setheading(90)
    player.forward(10)
    player.penup()

def down():
    player.setheading(270)
    player.forward(10)
    player.penup()

def right():
    player.setheading(0)
    player.forward(10)
    player.penup()

def left():
    player.setheading(180)
    player.forward(10)
    player.penup()

# drawing the actual maze
for i in range(25):

    if i > 4:
        # random variables
        door = random.randint(door_width, amount-2*door_width)
        barrier = random.randint(2*wall_width, amount-2*door_width)
        if (door < barrier):
            drawbot.forward(door) # go forward until door beginning

            # creating the gap

            drawbot.penup() 
            drawbot.forward(door_width)
            drawbot.pendown()

            drawbot.forward(barrier - door - door_width)

            drawbot.left(90) # turn to start drawing barrier
            drawbot.forward(barrier_length) # draw barrier
            drawbot.backward(barrier_length) # draw over barrier to cont. maze
            drawbot.right(90) # turn to cont. maze

            drawbot.forward(amount - barrier)

        else:
            drawbot.forward(barrier) # go forward until barrier beginning

            #draw barrier
            drawbot.left(90) # turn to start drawing barrier
            drawbot.forward(barrier_length) # draw barrier
            drawbot.backward(barrier_length) # draw over barrier to cont. maze
            drawbot.right(90) # turn to cont. maze

            #forward to door
            drawbot.forward(door - barrier) # go forward until door beginning

            # draw door
            drawbot.penup() 
            drawbot.forward(door_width)
            drawbot.pendown()

            drawbot.forward(amount - door_width - door) # finish maze wall

    drawbot.left(90)
    amount += wall_width

wn = trtl.Screen()

wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")

wn.listen()



wn.mainloop()