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

# This first loop is to assign the value for the vertices.
# It will iterate through the loop and depending on the value of i it will assign a value to the vertex
for i in range(9):
    if i == 0:
        vertices[i] = np.array([x, y, y])
    if i == 1:
        vertices[i] = np.array([x, x, y])
    if i == 2:
        vertices[i] = np.array([y, x, y])
    if i == 3:
        vertices[i] = np.array([y, y, y])
    if i == 4:
        vertices[i] = np.array([x, y, x])
    if i == 5:
        vertices[i] = np.array([x, x, x])
    if i == 6:
        vertices[i] = np.array([y, y, x])
    if i == 7:
        vertices[i] = np.array([y, x, x])

# This second loop will give the value to the 8 points we stored in the list called points
# It will iterate through the list called points then assigns the value
for i in range(8):
    # Using line equation to assign the value of the points
    points[i] = np.add(np.multiply(x, vertices[i]), p0)