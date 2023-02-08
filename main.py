#  Triangle Perimeter Asgn Python CS30

# Importing The Math Module For The Square Root Function
import math

# Functions
def dist(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance

# Getting Measurements From The User
xA = int(input("What is the xA value?:"))
yA = int(input("What is the yA value?:"))
xB = int(input("What is the xB value?:"))
yB = int(input("What is the yB value?:"))
xC = int(input("What is the xC value?:"))
yC = int(input("What is the yC value?:"))

AB = dist(xA, yA, xB, yB)
AC = dist(xA, yA, xC, yC)
BC = dist(xB, yB, xC, yC)

perimeter = AB + AC + BC


