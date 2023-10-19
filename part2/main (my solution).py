"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import random
import time
import turtle

#Scoreboard variables
FONT = ("Courier", 16, "normal")
ALIGNMENT = "center"
#CarManager variables
COLORS = ["red", "green", "blue", "purple", "orange", "yellow", "pink", "grey", "gold", 
          "lemon chiffon", "aquamarine"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
#Player Variables
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
  #Step 1
  def __init__(self):
    super().__init__()
    self.setheading(90)
    self.shape("turtle")
    self.penup()
    self.start_position()
    

  #Step 1
  def up(self):
    new_y = self.ycor() + MOVE_DISTANCE
    self.goto(self.xcor(), new_y)

  #step 1
  def start_position(self):
    self.goto(STARTING_POSITION)
    
  
class CarManager(turtle.Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.shape("square")
    self.shapesize(stretch_len=2, stretch_wid=1)
    self.select_color()
    self.select_y_position()

  def select_color(self):
    #choose random color
    self.color(random.choice(COLORS))

  def select_y_position(self):
    self.goto(300,random.randint(-245,250))

  def move(self):
    if self.xcor() > 0:
      move_x = self.xcor() - STARTING_MOVE_DISTANCE
    else:
      move_x = self.xcor() - MOVE_INCREMENT

    self.goto(move_x, self.ycor())
    

class Scoreboard(turtle.Turtle):
  #Step 1
  def __init__(self):
    super().__init__()
    self.penup()
    self.hideturtle()
    self.color("black")
    self.level = 1
    self.move_speed = 0.1
    self.refresh()
  #Step 1
  def refresh(self):
    self.clear()
    self.goto(-280, 280)
    self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

  #Step 1
  def add_level(self):
    self.level += 1
    self.move_speed *= 0.9
    self.refresh()

  def reset_score(self):
    self.level = 1
    self.move_speed = 0.1
    self.goto(0,0)
    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("grey45")
screen.tracer(0)

turtle = Player()
scoreboard= Scoreboard()
#car = CarManager()

# Begin!

cars_list = []

screen.listen()
screen.onkeypress(turtle.up,"Up")
screen.onkeypress(turtle.up,"w")

game_is_on = True
loop_time = 0

while game_is_on:
  time.sleep(scoreboard.move_speed)
  screen.update()
  #car.move()
  if loop_time % 6 == 0:
    car = CarManager()
    cars_list.append(car)
    
  for car in cars_list:
    car.move()
    if car.xcor() < -350:
      car.hideturtle()
      cars_list.remove(car)

    #detect collision with car
  for car in cars_list:
    if car.distance(turtle) < 20:
      game_is_on = False
      scoreboard.reset_score()
  
  #detect collision with finish line and upgrade level
  if turtle.ycor() > 290:
    turtle.start_position()
    scoreboard.add_level()
    #increase time speed


      

  loop_time += 1
    


screen.exitonclick()