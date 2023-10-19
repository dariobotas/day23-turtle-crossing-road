"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import time
import turtle

COLORS = ["red", "green", "blue", "purple", "orange", "yellow", "pink", "grey", "gold", 
          "lemon chiffon", "aquamarine"]
FONT = ("Courier", 16, "normal")
STARTIN_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION = (0, 180)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 180


class Player:
  pass
  
class CarManager:
  pass

class Scoreboard:
  pass


# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(600, 600)
screen.tracer(0)

# Begin!
game_is_on = True

while game_is_on:
  time.sleep(0.1)
  screen.update()