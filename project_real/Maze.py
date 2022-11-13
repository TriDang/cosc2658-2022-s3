import random

class Maze:
  def __init__(self):
    # Note: in my real test, I will create much larger
    # and more complicated map
    self.rows = 4
    self.cols = 5
    self.map = [ \
      ".....", \
      ".   X", \
      ".   .", \
      "....." ]
    self.robotRow = 2;
    self.robotCol = 1;
    self.steps = 0;

  def go(self, direction):
    if (direction != "UP" and \
        direction != "DOWN" and \
        direction != "LEFT" and \
        direction != "RIGHT"):
      # invalid direction
      self.steps += 1
      return "false"

    currentRow = self.robotRow
    currentCol = self.robotCol
    if (direction == "UP"):
      currentRow -= 1
    elif (direction == "DOWN"):
      currentRow += 1
    elif (direction == "LEFT"):
      currentCol -= 1
    else:
      currentCol += 1

    # check the next position
    if (self.map[currentRow][currentCol] == 'X'):
      # Exit gate
      self.steps += 1
      print("Steps to reach the Exit gate", self.steps)
      return "win"
    elif (self.map[currentRow][currentCol] == '.'):
      # Wall
      self.steps += 1
      return "false"
    else:
      # Space => update robot location
      self. steps += 1
      self.robotRow = currentRow
      self.robotCol = currentCol
      return "true";

class Robot:
  # A very simple implementation
  # where the robot just go randomly
  def navigate(self):
    maze = Maze()
    result = ""
    while (result != "win"):
      rnd = random.random()
      if (rnd <= 0.25):
        print("UP")
        result = maze.go("UP")
      elif (rnd <= 0.50):
        print("DOWN")
        result = maze.go("DOWN")
      elif (rnd <= 0.75):
        print("LEFT")
        result = maze.go("LEFT")
      else:
        print("RIGHT")
        result = maze.go("RIGHT")

Robot().navigate()
