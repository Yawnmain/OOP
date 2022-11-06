def matrix_check(m1, m2):
    return trueMat(m1) and trueMat(m2)
    
def trueMat(m):
    if type(m) != list:
        return False
    elif type(m) == list and cells_check(m):
        return True
    else:
        raise TypeError(type(m))

def cells_check(m):
    for row in m:
        if type(row) == list:
            for cell in row:
                if not(type(cell) in (int, float)):
                    mess = cell
                    raise TypeError(mess)
    return True

def size_check(m1, m2):
    if len(m1) == len(m2):
        for num in range(len(m1)):
            if len(m1[num]) != len(m2[num]):
                mess = "Lens are not similar"
                raise ValueError("Size error")
    else:
        mess = "Lens are not similar"
        raise ValueError(mess)

def mul_size_check(m1, m2):
    for row in m1:
        if len(row) != len(m2):
            raise ValueError("Size error")

def numOfMat(m, num):
    if type(m) == list:
        if trueMat(m) and cells_check(m) and type(num) in (int, float):
            return m, num
    elif type(num) == list:
        if trueMat(num) and cells_check(num) and type(m) in (int, float):
            return num, m
    else:
        raise TypeError("must be only list or num")