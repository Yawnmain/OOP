from matplotlib import pyplot as plt
import math as mat
from Macloren import *


def vis_exp(x, n):
    p_x = [i / 10 for i in range(-50, 50)]
    y = [exp(X, n) for X in p_x]
    plt.plot(p_x, y, color="blue")

    p_y = [exp(X, n) for X in p_x]
    y_point = exp(x, n)

    plt.title("exp")
    start(x, y_point, p_x, p_y)


def vis_cos(x, n):
    p_x = [i / 10 for i in range(-50, 50)]
    y = [cos(X, n) for X in p_x]
    plt.plot(p_x, y, color="blue")

    p_y = [cos(X, n) for X in p_x]
    y_point = cos(x, n)

    plt.title("cos")
    start(x, y_point, p_x, p_y)


def vis_sin(x, n):
    p_x = [i / 10 for i in range(-50, 50)]
    y = [sin(X, n) for X in p_x]
    plt.plot(p_x, y, color="blue")

    p_y = [sin(X, n) for X in p_x]
    y_point = sin(x, n)

    plt.title("sin")
    start(x, y_point, p_x, p_y)


def start(x, y, p_x, p_y):
    plt.plot(p_x, p_y, color="blue")
    plt.scatter(x, y, color="orange")
    plt.grid()
    plt.show()


x, n = 1, 5

vis_exp(x, n)
vis_cos(x, n)
vis_sin(x, n)
