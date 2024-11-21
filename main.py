# Donovan Farley-Freeman
# 11/18/24
# Creating a fractal tree with turtle in python

import turtle as terry
from random import randint
"""
IMPORTANT
To run your code in this project,
open the Terminal and enter the following:

python main.py    then enter

Your output will be visualized in the 
Virtual Desktop
"""

DECVAL = 0.75
AOT = 30
STARTLEN = 75
STARTHICK = 15
LEAFCOLOR = 'DarkGreen'
TRUNKCOLOR = 'burlywood4'

def fractree(length, thick, child, trunk=False):
  # Base case
  if (length <= 10) or (child == 0):
    return

  # When to change to create leafs
  elif length*DECVAL <= 10:
    terry.color(LEAFCOLOR)
    thick = STARTHICK/DECVAL

  # For creating the trunk
  elif trunk is True:
    terry.color(TRUNKCOLOR)
    terry.left(90)
    terry.pensize(STARTHICK)
    terry.speed(1)
    terry.forward(STARTLEN)

  # Recursion
  if child == 1:
    if randint(1,2) == 1:
      leftdif = left(length*DECVAL, thick*DECVAL)
      terry.backward(length*DECVAL)
      terry.right((AOT/2.0)+leftdif)
    else:
      rightdif = right(length*DECVAL, thick*DECVAL)
      terry.backward(length*DECVAL)
      terry.left((AOT/2.0)+rightdif)

  elif child == 2:
    leftdif = left(length*DECVAL, thick*DECVAL)
    terry.backward(length*DECVAL)
    terry.right((AOT/2.0)+leftdif)

    rightdif = right(length*DECVAL, thick*DECVAL)
    terry.backward(length*DECVAL)
    terry.left((AOT/2.0)+rightdif)

  terry.color(TRUNKCOLOR)

def left(length, thick):
  angdif = randint(-5,5)
  terry.pensize(thick)
  terry.left((AOT/2.0)+angdif)
  terry.forward(length)
  terry.pensize(0)
  fractree(length, thick, randint(0,2))
  return angdif

def right(length, thick):
  angdif = randint(-5,5)
  terry.pensize(thick)
  terry.right((AOT/2.0)+angdif)
  terry.forward(length)
  terry.pensize(0)
  fractree(length, thick, randint(0,2))
  return angdif

fractree(STARTLEN, STARTHICK, randint(0,2), True)

terry.mainloop()