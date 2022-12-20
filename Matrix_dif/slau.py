import MYmatrix as mt
import class_vector as v
from copy import deepcopy

# Interpolar part


def slau_for_inter(m, keys):
    new_m = deepcopy(m)
    new_k = deepcopy(keys)
    randomaizer_rows(new_m, new_k)
    new_m, new_k = gaus_drive_sub(new_m, new_k)
    new_m, new_k = gaus_reverse_sub(new_m, new_k)

    return new_k

# Gauss


def randomaizer_rows(m, key):
    for i in range(len(m)):
        if m[i][i] == 0:
            for j in range(len(m)):
                if m[j][i] != 0 and m[i][j] != 0:
                    mt.change_rows(m, i, j)
                    tmp = key[i]
                    key[j] = key[i]
                    key[i] = tmp
                    break


def gaus_slau(m, key):
    mt.matrix_check(m, key)
    new_m = deepcopy(m)
    new_k = deepcopy(key)
    randomaizer_rows(new_m, new_k)
    new_m, new_k = gaus_drive_sub(new_m, new_k)
    new_m, new_k = gaus_reverse_sub(new_m, new_k)
    return new_k


def gaus_drive_sub(m, key):
    keys_matrix = mt.trueMat(key)
    for i in range(len(m)):
        for j in range(i + 1):
            if i != j:
                if m[i][j] != 0:
                    if m[j][j] == 0:
                        mt.change_rows(m, i, j)
                        if keys_matrix:
                            mt.change_rows(key, i, j)
                        else:
                            tmp = key[j]
                            key[j] = key[i]
                            key[i] = tmp
                    if keys_matrix:
                        key = mt.sub_rows(key, i, j, m[i][j])
                    else:
                        key[i] -= key[j] * m[i][j]
                    m = mt.sub_rows(m, i, j, m[i][j])
            else:
                if m[i][i] == 0:
                    continue
                elif m[i][i] != 1:
                    if keys_matrix:
                        key = mt.mul_row(key, i, 1 / m[i][i])
                    else:
                        key[i] /= m[i][i]
                    m = mt.mul_row(m, i, 1 / m[i][i])
    return m, key


def gaus_reverse_sub(m, key):
    keys_matrix = mt.trueMat(key)
    for i in range(len(m) - 1, -1, -1):
        for j in range(len(m) - 1, -1, -1):
            if i != j:
                if m[i][j] != 0:
                    if keys_matrix:
                        key = mt.sub_rows(key, i, j, m[i][j])
                    else:
                        key[i] -= key[j] * m[i][j]
                    m = mt.sub_rows(m, i, j, m[i][j])
            else:
                if m[i][i] != 1:
                    if keys_matrix:
                        key = mt.mul_row(key, i, 1 / m[i][i])
                    else:
                        key[i] /= m[i][i]
                    m = mt.mul_row(m, i, 1 / m[i][i])
    return m, key


# Reverse method


def reverse_matrix(m):
    diagonal_mat = diag_matrix(len(m))
    return gaus_slau(m, diagonal_mat)


def reverse_slau(m, key):
    return mt.mul(reverse_matrix(m), key)


def diag_matrix(size):
    m = []
    for i in range(size):
        tmp = []
        for j in range(size):
            if i == j:
                tmp += [1]
            else:
                tmp += [0]
        m += [tmp]
        tmp = []
    return m
