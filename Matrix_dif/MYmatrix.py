import class_vector as v
import error_lib as e
from copy import deepcopy

# возврат строки


def retRow(a, row):
    return a[row]

# замена строк


def change_rows(a, r1, r2, flag=False):
    if flag:
        a = deepcopy(a)
    tmp = retRow(a, r2)
    a[r2] = a[r1]
    a[r1] = tmp
    return a


def add(a, b):
    new_m = []
    if e.matrix_check(a, b):
        e.size_check(a, b)
        for row in range(len(a)):
            new_m += [v.add(a[row], b[row])]
    else:
        mat, scal = e.numOfMat(a, b)
        for row in mat:
            new_m += [v.add(row, scal)]
    return new_m


def mul(a, b):
    new_m = []
    if e.matrix_check(a, b):
        e.mul_size_check(a, b)
        for i in range(len(a)):
            tmp = []
            for c in range(len(b)):
                cell_tmp = 0
                for j in range(len(a[c])):
                    cell_tmp += a[i][j] * b[j][c]
                tmp += [cell_tmp]
            new_m += [tmp]
    else:
        mat, scal = e.numOfMat(a, b)
        for row in mat:
            new_m += [v.mul(row, scal)]
    return new_m


def mul_row(a, row, scalar=1):
    e.trueMat(a)
    new_m = deepcopy(a)
    for i in range(len(new_m[row - 1])):
        new_m[row][i] *= scalar
    return new_m


def sub(a, b):
    if e.matrix_check(a, b):
        return add(a, mul(b, -1))
    else:
        mat, scal = e.numOfMat(a, b)
        return add(mat, 0 - scal)


def add_rows(a, r1, r2, scalar=1):
    e.trueMat(a)
    new_m = deepcopy(a)
    new_m[r1] = v.add(new_m[r1], v.mul(retRow(new_m, r2), scalar))
    return new_m


def sub_rows(a, r1, r2, scalar=1):
    e.matrix_check(a)
    new_m = deepcopy(a)
    new_m[r1 - 1] = v.sub(new_m[r1 - 1],
                          v.mul(retRow(new_m, r2), scalar))
    return new_m
