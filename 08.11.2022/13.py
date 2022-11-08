import random
import time


n = int(input('n: '))
arr = [random.randint(1, 100) for _ in range(n)]
print(sum(arr))
s = 0


def sumList(x, i=0):
    if i >= len(arr):
        return 0
    return x[i] + sumList(arr, i + 1)


start_time1 = time.time()
print(sumList(arr))
print("--- %s seconds ---" % (time.time() - start_time1))
