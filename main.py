"""
Instructor solution:
1º Move the turtle with keypress
2º Create and move the cars
3º Detect collision with car
4º Detect when turtle reaches the other side
5º Create a scoreboard
"""

import random
import time
import turtle

#Player variables
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
#CarManager Variables
COLORS = ["red", "green", "blue", "purple", "orange", "yellow", "pink", "grey", "gold", 
          "lemon chiffon", "aquamarine"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
#Scoreboard variables
FONT = ("Courier", 16, "normal")
ALIGNMENT = "center"

class Player(turtle.Turtle):
  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.penup()
    self.go_to_start()
    self.setheading(90)

  def up(self):
    self.forward(MOVE_DISTANCE)

  def go_to_start(self):
    self.goto(STARTING_POSITION)

  def is_at_finish_line(self):
    return self.ycor() > FINISH_LINE_Y
    

class CarManager(turtle.Turtle):
  def __init__(self):
    super().__init__()
    self.all_cars = []
    self.car_speed = STARTING_MOVE_DISTANCE

  def create_car(self):
    random_chance = random.randint(1,6)
    if random_chance == 1:
      new_car = turtle.Turtle("square")
      new_car.shapesize(stretch_wid=1, stretch_len=2)
      new_car.penup()
      new_car.color(random.choice(COLORS))
      new_car.goto(x=300,y=random.randint(-250,250))
      self.all_cars.append(new_car)

  def move_cars(self):
    for car in self.all_cars:
      car.backward(self.car_speed)

  def level_up(self):
    self.car_speed += MOVE_INCREMENT    


class Scoreboard(turtle.Turtle):
  #Step 1
  def __init__(self):
    super().__init__()
    self.level = 1
    self.hideturtle()
    self.penup()
    self.goto(-280, 260)
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
  
  def increase_level(self):
    self.level += 1
    self.update_scoreboard()

  def game_over(self):
    self.goto(0, 0)
    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey45")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard= Scoreboard()

# Begin!
screen.listen()
screen.onkeypress(player.up,"Up")
screen.onkeypress(player.up,"w")

game_is_on = True
loop_time = 0

while game_is_on:
  time.sleep(0.1)
  screen.update()

  car_manager.create_car()
  car_manager.move_cars()

  #Detect car collision
  for car in car_manager.all_cars:
    if car.distance(player) < 20:
      game_is_on = False
      scoreboard.game_over()

  #Detect successful crossing
  if player.is_at_finish_line():
    player.go_to_start()
    car_manager.level_up()
    scoreboard.increase_level()
    

screen.exitonclick()