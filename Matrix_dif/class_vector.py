import math


def lenght(v1):
    tmp = 0
    for coord in v1:
        tmp += coord * coord
    return math.sqrt(tmp)

def add(v1, v2):
    if trueVector(v1,v2):
        return [v1[i] + v2[i] for i in range(len(v1))]
    else:
        v, num = check_type(v1, v2)
        return [v[i] + num for i in range(len(v))]

def mul(vec1, vec2):
    if trueVector(vec1, vec2):
        return [(vec1[i] * vec2[i]) for i in range(len(vec1))]
    else:
        v, num = check_type(vec1, vec2)
        return [v[i] * num for i in range(len(v))]

def sub(v1, v2):
    if trueVector(v1,v2):
        return [v1[i] - v2[i] for i in range(len(v1))]  
    else:
        v, num = check_type(v1, v2)
        return [v[i] - num for i in range(len(v))]
    
def div(v1,v2):
    if trueVector(v1,v2):
        v = []
        for i in range(len(v1)):
            v.append(v1[i]/v2[i])
        return v

def scalar_div(v1, scalar):
    v = []
    for i in range(len(v1)):    
        v.append(v1[i] / scalar)
    return v 

def scalar_mlt(v1, v2):
    trueVector(v1,v2)
    v = 0
    for i in range(len(v1)):    
        v += (v1[i] * v2[i])
    return v

def coll(v1, v2):
    trueVector(v1,v2)
    n = 5
    return abs(Cos(v1,v2, n)) == 1

def directed_vs(v1,v2):
    trueVector(v1,v2)
    n = 5
    return abs(Cos(v1,v2, n)) == 1

def eq_vs(v1, v2):
    trueVector(v1,v2)
    n = 0
    for i in range(len(v1)):
        if abs(v1[i] - v2[i]) > n:
            return False
    return True

def ort(v1,v2):
    trueVector(v1,v2)
    n = 5
    return Cos(v1, v2, n) == 0

def Norm_of_vector(v1, _len_a):
    return div(v1, lenght(v1))

def change_dir(v1):
    v = []
    for i in range(len(v1)):
        v.append(v1[i]*(-1))
    return v

def angle(v1,v2):
    trueVector(v1,v2)
    n = 5
    cos = Cos(v1,v2)
    rd = math.acos(cos)
    return round(rd / math.pi * 180 , 3)        

def projection(v1, v2):
    trueVector(v1,v2)
    return scalar_mlt(v1,v2) / lenght(v2)

def Cos(v1,v2):
    trueVector(v1,v2)
    return scalar_mlt(v1,v2) / (lenght(v1) * lenght(v2))

def trueVector(v1, v2):
    if type(v1) != list or type(v2) != list:
        return False
    checkSize(v1, v2)
    return True

def checkSize(v1, v2):
    if len(v1) != len(v2):
        mess = "Lens are not similar"
        raise ValueError(mess)
    return True

def check_type(v, num):
    if type(v) == list:
        if type(num) in (int, float):
            return v, num
    elif type(num) == list:
        if type(v) in (int, float):
            return num, v