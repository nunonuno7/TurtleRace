from turtle import *
import random
from random import randint

screen = Screen()

color = ["red","green","blue","black","purple","orange"]
    
def draw_finish_line(end):
    line = Turtle()
    line.speed(1000)
    line.penup()
    line.goto(end,-600)
    line.pensize(3)
    line.pendown()
    line.goto(end,+600)


finish_line = 340

draw_finish_line(finish_line) 

# Create turtles
start_y = -250
start_x = -340
turtles = []

turtle_number = int(screen.numinput("Turtle Number", "How many turtles will compete (1 to 6)?", default=6, minval=1, maxval=6))

for i in range(0,turtle_number):
    turtle = Turtle(shape="turtle")
    turtle.color(color[i])
    turtles.append(turtle)
    turtle.penup()
    turtle.goto(start_x,start_y+i*50)
    start_y += 50

user_bet = screen.textinput(title="Make your Bet", prompt="Whick turtle will win the race? Enter a color: ")

positions = [finish_line-1]

while max(positions) < finish_line:
    positions = []
    for turtle in turtles:
        turtle.speed(random.randint(1, 5))
        turtle.forward(random.randint(1, 10))
        corrent_position = turtle.position()[0]
        positions.append(corrent_position)
        
winer_position = max(positions)

winer_index = positions.index(winer_position)

winning_color = turtles[winer_index].color()[0]

print(f'The {winning_color} Turtle Won !!')


result_text = Turtle()
result_text.penup()
result_text.goto(0, -250)
result_text.hideturtle()

# Check user's bet
if winning_color == user_bet:
    result_text.write(f"Congratulations! You Win! \nThe winning color was {winning_color}.", align="center", font=("Arial", 24, "bold"))
else:
    result_text.write(f"Sorry, You Lose! \nThe winning color was {winning_color}.", align="center", font=("Arial", 24, "bold"))

exitonclick()