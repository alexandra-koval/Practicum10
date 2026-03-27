import turtle
import math


def parallelogram(x, y, a, b, c):
    '''
    Function, drawing parallelogram.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: the length of one side of a parallelogram
    :param b: the length of second side of a parallelogram
    :param c: the degree measure of one of the angles of a parallelogram
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('purple')
    turtle.begin_fill()
    c1 = 180 - c
    turtle.forward(a)
    turtle.left(c)
    turtle.forward(b)
    turtle.left(c1)
    turtle.forward(a)
    turtle.left(c)
    turtle.forward(b)
    turtle.left(c1)
    turtle.end_fill()


def triangle_ravnobedren(x, y, a, b):
    '''
    Function, drawing triangle_ravnobedren.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: the length of one side of a triangle_ravnobedren
    :param b: the length of second side of a triangle_ravnobedren
    :return: None
    '''
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.fillcolor('pink')
    turtle.begin_fill()
    turtle.forward(a)
    h = math.sqrt(b ** 2 - (a / 2) ** 2)
    angle = math.degrees(math.atan2(h, a / 2))
    turtle.left(180 - angle)
    turtle.forward(b)
    turtle.left(2 * angle)
    turtle.forward(b)
    turtle.end_fill()
    turtle.left(180 - angle)


def square(x, y, a):
    '''
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a square
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('violet')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()


def triangle_pryamougoln(x, y, a, b):
    '''
    Function, drawing triangle_pryamougoln.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: the length of one side of a triangle_pryamougoln
    :param b: the length of second side of a triangle_pryamougoln
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    h = math.sqrt(a ** 2 + b ** 2)
    angle = math.degrees(math.atan2(b, a))
    turtle.left(90 + angle)
    turtle.forward(h)
    turtle.end_fill()


def dog():
    '''
    Dog function.
    :return: None
    '''
    turtle.setheading(0)
    triangle_pryamougoln(0, 0, 75, 75)
    turtle.setheading(0)
    triangle_pryamougoln(75, 75, 150, 150)
    turtle.right(45)
    triangle_pryamougoln(150, 150, 150, 150)
    turtle.left(90)
    triangle_ravnobedren(0, 150, 100, 65)
    turtle.setheading(0)
    square(150, 75, 75)
    triangle_ravnobedren(225, 150, 100, 75)
    turtle.setheading(48)
    parallelogram(225, 150, 75, 75, 42)


dog()
