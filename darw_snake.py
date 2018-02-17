import turtle
from random import *

def darw_snake(rad, angle, len, neckrad):
    for i in range(len):
        # turtle.circle()画一个半径为rad，弧度为angle的圆
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle / 2)
    # turtle.fd()=turtle.forward(),沿直线爬行多长
    turtle.fd(rad)
    turtle.circle(neckrad + 1, 180)
    turtle.fd(rad * 2 / 3)
    

def main():
    turtle.setup(1300, 800, 100, 80)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    # 运行角度,0度向右
    turtle.seth(-40)
    darw_snake(40, 80, 5, pythonsize / 2)

def name():
    # turtle.circle(80, 180)
    # turtle.seth(-90)
    # turtle.fd(300)
    print(random())

# main()
name()