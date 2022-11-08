import random
import time

n = int(input('n: '))
arr = [random.randint(1, 100) for _ in range(n)]
print(arr)

# 1
start_time1 = time.time()
print(arr[-1])
print("--- %s seconds ---" % (time.time() - start_time1))

# 2
start_time2 = time.time()
for i in range(0, len(arr)):
    if i == (len(arr)-1):
        print("The last element of list using loop : "
              + str(arr[i]))
print("--- %s seconds ---" % (time.time() - start_time2))
# 3
start_time3 = time.time()
arr.reverse()
print("The last element of list using reverse : "
      + str(arr[0]))
print("--- %s seconds ---" % (time.time() - start_time3))
