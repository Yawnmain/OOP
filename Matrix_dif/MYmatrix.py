import class_vector as v
from copy import deepcopy

# возврат строки


def GetRow(a, row):
    return a[row]

# замена строк


def change_rows(a, r1, r2, flag=False):
    if flag:
        a = deepcopy(a)
    tmp = GetRow(a, r2)
    a[r2] = a[r1]
    a[r1] = tmp
    return a


def add(a, b):
    new_m = []
    if matrix_check(a, b):
        size_check(a, b)
        for row in range(len(a)):
            new_m += [v.add(a[row], b[row])]
    else:
        mat, scal = numOfMat(a, b)
        for row in mat:
            new_m += [v.add(row, scal)]
    return new_m


def mul_size_check(m1, m2):
    for row in m1:
        if len(row) != len(m2):
            raise ValueError("Size error")


def mul(a, b):
    new_m = []
    if matrix_check(a, b):
        mul_size_check(a, b)
        if (trueMat(b)):
            for i in range(len(a)):
                tmp = []
                for c in range(len(b)):
                    cell_tmp = 0
                    for j in range(len(a[c])):
                        cell_tmp += a[i][j] * b[j][c]
                    tmp += [cell_tmp]
                new_m += [tmp]
        else:
            for i in range(len(a)):
                for c in range(len(b)):
                    cell_tmp = 0
                    for j in range(len(a[c])):
                        cell_tmp += a[i][j] * b[j]
                new_m += [cell_tmp]
    else:
        mat, scal = numOfMat(a, b)
        for row in mat:
            new_m += [v.mul(row, scal)]
    return new_m


def mul_row(a, row, scalar=1):
    trueMat(a)
    new_m = deepcopy(a)
    for i in range(len(new_m[row - 1])):
        new_m[row][i] *= scalar
    return new_m


def sub(a, b):
    if matrix_check(a, b):
        return add(a, mul(b, -1))
    else:
        mat, scal = numOfMat(a, b)
        return add(mat, 0 - scal)


def add_rows(a, r1, r2, scalar=1):
    trueMat(a)
    new_m = deepcopy(a)
    new_m[r1] = v.add(new_m[r1], v.mul(GetRow(new_m, r2), scalar))
    return new_m


def sub_rows(a, r1, r2, scalar=1):
    trueMat(a)
    new_m = deepcopy(a)
    new_m[r1] = v.sub(new_m[r1],
                      v.mul(GetRow(new_m, r2), scalar))
    return new_m

# from error_lib func


def type_of_cells(m):
    for row in m:
        if type(row) == list:
            for cell in row:
                if not (type(cell) in (int, float)):
                    raise
        else:
            return False
    return True


def trueMat(m):
    if type(m) != list:
        return False
    elif type(m) == list:
        if type_of_cells(m):
            return True
    else:
        raise


def matrix_check(m1, m2):
    return (trueMat(m1) and trueMat(m2)) or (trueMat(m1) and v.vector_check(m2))


def size_check(m1, m2):
    if len(m1) == len(m2):
        for row in range(len(m1)):
            if len(m1[row]) != len(m2[row]):
                raise
    else:
        raise


def numOfMat(m, num):
    if type(m) == list:
        if trueMat(m) and type_of_cells(m) and type(num) in (int, float):
            return m, num
    elif type(num) == list:
        if trueMat(num) and type_of_cells(num) and type(m) in (int, float):
            return num, m
    else:
        raise
