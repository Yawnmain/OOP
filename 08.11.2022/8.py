import time


def pif(n, m):
    arr = []
    for i in range(n, m):
        for j in range(n, m):
            for z in range(n, m):
                if i**2 + j**2 == z**2:
                    arr.append([i, j, z])
    return arr


n, m = (input("n: "), input("m: "))
n, m = int(n), int(m)
start_time = time.time()
x = [print(el) for el in pif(n, m)]
print("--- %s seconds ---" % (time.time() - start_time))
