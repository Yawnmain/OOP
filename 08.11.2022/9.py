import time


def div(x):
    num = x
    while(num):
        p = num % 10
        num //= 10
        if (p == 0) or (x % p):
            return False
    return True


n, m = input("n: "), input("m: ")
n, m = int(n), int(m)

start_time = time.time()
for i in range(n, m):
    if (div(i)):
        print(i)
print("--- %s seconds ---" % (time.time() - start_time))
