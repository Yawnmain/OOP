import time
start_time = time.time()
while True:
    try:
        N = int(input('N: '))
        arr = []
        for i in range(N):
            arr.append(int(input("Put a num: ")))
        for j in arr:
            flag = True
            if isinstance(j, int):
                flag = True
            else:
                flag = False
        if flag == True:
            print(sum(arr))
            print("--- %s seconds ---" % (time.time() - start_time))
            break
        else:
            print('Try again')
    except ValueError:
        print("Type error")
        print("--- %s seconds ---" % (time.time() - start_time))
