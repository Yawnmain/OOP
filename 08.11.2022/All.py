import time
from memory_profiler import profile
import random
from tkinter import *
from tkinter import ttk


@profile
def t1():
    start_time = time.time()
    a, b, c = [input('a: '), input('b: '), input('c: ')]
    a, b, c = b, c, a
    print(a, b, c)
    print("--- %s seconds ---" % (time.time() - start_time))


@profile
def t2_1_2_2():
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


@profile
def t3_1():
    start_time = time.time()
    x = random.randint(0, 100)
    print(f'x: {x}', x**5)
    print("--- %s seconds ---" % (time.time() - start_time))


@profile
def t3_2():
    start_time = time.time()
    x = random.randint(0, 100)
    print(f'x: {x}')
    y = x*x*x*x*x
    print(y)
    print("--- %s seconds ---" % (time.time() - start_time))


@profile
def t4():
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


@profile
def t5():
    def first():
        start_time = time.time()
        m = int(input('Put a mnth 1-12 : '))
        if m == 1 or m == 2 or m == 12:
            print('Winter')
        elif m == 3 or m == 4 or m == 5:
            print('Sping')
        elif m == 6 or m == 7 or m == 8:
            print('Summer')
        elif m == 9 or m == 10 or m == 11:
            print('Autumn')
        else:
            print('Error')
        print("--- %s seconds ---" % (time.time() - start_time))

    def second():
        start_time = time.time()
        a = {'Winter': (1, 2, 12),
             'Sping': (3, 4, 5),
             'Summer': (6, 7, 8),
             'Autumn': (9, 10, 11)}

        mnth = int(input('Put a mnth 1-12: '))
        for key in a.keys():
            if mnth in a[key]:
                print(key)
        print("--- %s seconds ---" % (time.time() - start_time))

    N = int(input("Choose a def 1-2: "))
    if N == 1:
        first()
    if N == 2:
        second()
    else:
        exit


@profile
def t6():
    N = int(input('N: '))
    cht = 0
    count_cht = 0
    ncht = 0
    count_ncth = 0
    i = 0
    start_time = time.time()
    while i <= N:
        if i % 2 == 0:
            cht += i
            count_cht += 1
        if i % 2 != 0:
            ncht += i
            count_ncth += 1
        i += 1

    print(f"Sum of cht: {cht}", "\n" f"Sum of ncht: {ncht}", "\n",
          f"Count of cht: {count_cht}", '\n', f"Count of cht: {count_ncth}")
    print("--- %s seconds ---" % (time.time() - start_time))


@profile
def t7():
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


@profile
def t8():
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


@profile
def t9():
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


@profile
def t10():
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


@profile
def t11():
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


@profile
def t12():
    n = int(input('n: '))
    arr = [random.randint(1, 100) for _ in range(n)]
    print(arr)
    start_time1 = time.time()
    arr.reverse()
    print(arr)
    print("--- %s seconds ---" % (time.time() - start_time1))


@profile
def t13():
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


@profile
def t14_1_2():
    test = Tk()
    test.title("Test")
    test.geometry("400x400")

    def R_to_D():
        dollar = 61.24
        price = rub.get()
        result.delete(1.0, END)
        result.insert(INSERT, float(price) /
                      float(dollar), INSERT, " долларов")

    def D_to_R():
        dollar = 61.24
        price = rub.get()
        result.delete(1.0, END)
        result.insert(INSERT, float(price) *
                      float(dollar), INSERT, " рублей")

    appName = Label(test, text="Рубли в доллары", font=(
        "arial", 30), fg="black")
    appName.place(x=45, y=30)

    result = Text(test, height=4, width=30,
                  font=("arial", 10))
    result.place(x=100, y=80)

    text = Label(test, text="Сумма",
                 font=("arial", 8, "bold"), fg="black")
    text.place(x=5, y=185)

    rub = Entry(test, font=("arial", 15))
    rub.place(x=100, y=180)

    button = Button(test, text="Rub to Dol", fg="red",
                    font=("arial", 20), bg="black", command=R_to_D)
    button.place(x=100, y=230, height=40, width=225)
    button = Button(test, text="Dol to Rub", fg="red",
                    font=("arial", 20), bg="black", command=D_to_R)
    button.place(x=100, y=280, height=40, width=225)

    test.mainloop()


@profile
def t15():
    n, m = input("n: "), input("m: ")
    start_time1 = time.time()
    n, m = int(n), int(m)
    if (n > 20) or (m > 20) or (n < 5) or (m < 5):
        exit
    else:
        for i in range(1, n+1):
            for j in range(1, m+1):
                print(i*j, end='\t')
            print()
    print("--- %s seconds ---" % (time.time() - start_time1))


@profile
def t16():
    def drawMatrix(matrix):
        for i in matrix:
            for j in i:
                print(j, end='\t')
            print()


t16()
