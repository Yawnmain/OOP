from slau import slau_for_inter
from copy import deepcopy

# 1


def koff(m):
    new_m = deepcopy(m)
    keys = []
    for i in range(len(new_m)):
        keys += [new_m[i][1]]
        new_m[i][1] = 1
    return slau_for_inter(new_m, keys)


def single_inter(m, x):
    koffs = koff(m)
    if type(x) in (float, int):
        return [x, koffs[0] * x + koffs[-1]]
    elif type(x) == list:
        points_arr = []
        for i in x:
            points_arr += [[i, koffs[0] * i + koffs[-1]]]
        return points_arr

# 2


def part_inter(m, x):
    koffs = []
    parts = []
    for i in range(len(m) - 1):
        koffs += [koff([m[i], m[i+1]])]
        parts += [[m[i][0], m[i+1][0]]]
    points_arr = []
    for j in x:
        if j <= parts[0][0]:
            points_arr += [[j, j * koffs[0][0] + koffs[0][1]]]
        elif j >= parts[-1][0]:
            points_arr += [[j, j * koffs[-1][0] + koffs[-1][1]]]
        else:
            for i in range(len(parts)):
                if j >= parts[i][0] and j <= parts[i][1]:
                    points_arr += [[j, j * koffs[i][0] + koffs[i][1]]]
    return points_arr

# 3


def basis(data_xy, j, x):
    l = 1
    for i in range(len(data_xy)):
        if i != j:
            l *= (x - data_xy[i][0]) / (data_xy[j][0] - data_xy[i][0])
    return l


def Lagrange(data_xy, x):
    L = 0
    for j in range(len(data_xy)):
        L += data_xy[j][1] * basis(data_xy, j, x)
    return [x, L]
