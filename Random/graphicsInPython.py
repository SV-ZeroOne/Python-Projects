import turtle 
#Cartesian coordinate systems! pair(x,y) 
# turtle library will work only with python 2, thus cant install the package in python 3
'''
turtle is old (last updated at 2009); it certainly Python2-only.

SyntaxError for except ValueError, ve: means that you're trying to install it with Python3. To use turtle you most certainly need Python 2.7.
'''

turtle.forward(90)
turtle.right(120)
turtle.forward(90)
turtle.right(120)
turtle.forward(90)

frankTheTurtle = turtle.Turtle()
for i in [0,1,2,3]:
    frankTheTurtle.forward(50)
    frankTheTurtle.left(90)

