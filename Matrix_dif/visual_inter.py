from matplotlib import pyplot as plt
import interpolar as interp


def vis_single_inter(mA):
    x, y = [], []
    for elem in mA:
        x += [elem[0]]
        y += [elem[1]]

    plt.title("Уравнение линии")
    start(x, y)


def vis_part_inter(mA, x_from_test):

    x, y = [], []
    data_x, data_y = [], []

    xy = interp.part_inter(mA, x_from_test)
    for elem in xy:
        x += [elem[0]]
        y += [elem[1]]

    for elem in mA:
        data_x += [elem[0]]
        data_y += [elem[1]]

    plt.title("Кусочно-линейная интерполяция")
    start(data_x, data_y)


def start(x, y):
    plt.plot(x, y)
    plt.grid()
    plt.show()


mA = [[2, 5], [6, 9]]

vis_single_inter(mA)

mA3 = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
x3 = [-1.5, 3, 2, 5, 9]

vis_part_inter(mA3, x3)
