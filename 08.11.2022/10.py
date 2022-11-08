import time
count = 0
start_time = time.time()
for i in range(0, 9000):
    s = 1
    j = 2
    while(j**2 <= i):
        if i % j == 0:
            s += j
            k = i//j
            if j != k:
                s += k
        j += 1
    if (s == i):
        count += 1
        if count < 6:
            print(i)
print("--- %s seconds ---" % (time.time() - start_time))
