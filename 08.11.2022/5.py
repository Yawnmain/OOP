import time


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
