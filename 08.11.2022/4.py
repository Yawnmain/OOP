import time
start_time = time.time()
x = int(input("Put a num 0-250: "))
if (x < 0) or (x > 250):
    print("Try again")
    exit
else:
    a, b = 0, 1
    while a+b <= x:
        a, b = b, a+b
    if x == b:
        print("Yes")
    else:
        print("No")
print("--- %s seconds ---" % (time.time() - start_time))
