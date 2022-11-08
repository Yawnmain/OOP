import random
import time

n = int(input('n: '))
arr = [random.randint(1, 100) for _ in range(n)]
print(arr)
start_time1 = time.time()
arr.reverse()
print(arr)
print("--- %s seconds ---" % (time.time() - start_time1))
