from matplotlib import pyplot as plt
from approx import *


def vis_line_approx(data_xy, x):
    x_from_test = x
    x = [line_approx(data_xy, [i])[0]
         for i in range(min(x_from_test) - 10, max(x_from_test) + 10)]
    y = [line_approx(data_xy, x[i])[1] for i in range(len(x))]

    plt.title("Линейная аппроксимация")
    start(x, y)


def start(x, y):
    plt.plot(x, y)
    plt.grid()
    plt.show()


xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
x = [4]

vis_line_approx(xy, x)
