# This program will build a rotating cube using python
# For this program to work some packages will need to be installed
# In order to install these packages you can run this command on the terminal of your IDE
# pip install pygame
# pip install numpy

# Import statements
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# We can control the size of the cube by altering the value of x
# We can control the place of rotation of the cube with altering the value of y
x = 1
y = -1
p0 = np.array([0, 0, 0])

# Let us put all 8 points into a list called points
# We will give value to these points later on
# Since p0 is a more or less constant point we don't have to declare it in a list like we did with other points
points = ['p1','p2','p3','p4','p5','p6','p7','p8']

# Let us also put all 8 vertices into a list called vertices
# We will assign a value to these vertices later on
vertices = ['v1','v2','v3','v4','v5','v6','v7','v8']
