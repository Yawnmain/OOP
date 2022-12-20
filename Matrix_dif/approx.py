from slau import slau_for_inter
from MYmatrix import *

# 1


def MNK(arr):
    A = []
    b = []
    koffs = []
    for i in range(len(arr)):
        k_list = []
        for j in range(len(arr[i])):
            k_list += [arr[i][j]]
        koffs += [k_list]

    for j in range(len(koffs) - 1):
        b += [0]
        for i in range(len(koffs)):
            b[-1] += koffs[i][j] * koffs[i][-1]

    for j in range(len(koffs) - 1):
        row_A = [0 for i in range(len(koffs) - 1)]
        for c in range(len(row_A)):
            for i in range(len(koffs)):
                row_A[c] += koffs[i][c] * koffs[i][j]
        A += [row_A]

    return slau_for_inter(A, b)

# 2


def trans(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def line_approx(data_xy, x):
    A = [[data_xy[i][0], 1] for i in range(len(data_xy))]
    b = [[data_xy[i][-1]] for i in range(len(data_xy))]
    A_data = mul(trans(A), A)
    b_data = [v[0] for v in mul(trans(A), b)]
    koffs = slau_for_inter(A_data, b_data)

    return [[el, koffs[0] * el + koffs[1]] for el in x]

# 3


def approx_by_polynomial(koffs, x):
    A = []
    b = [[el] for el in koffs]
    for i in range(len(x)):
        row_A = []
        for j in range(len(koffs)):
            row_A = [x[i]**j] + row_A
        A += [row_A]
    y = mul(A, b)

    return [[x[i], y[i][0]] for i in range(len(y))]
