import time


def divis(n):
    start_time = time.time()
    count = 0
    for i in range(1, int(n+1)):
        if n % i == 0:
            count += 1
    print("--- %s seconds ---" % (time.time() - start_time))
    return count


n = int(input("Put a num 1-249: "))
if (n > 249) or (n < 1):
    exit
else:
    print(divis(n))
