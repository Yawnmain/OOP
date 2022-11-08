import time
start_time = time.time()
a, b, c = [input('a: '), input('b: '), input('c: ')]
a, b, c = b, c, a
print(a, b, c)
print("--- %s seconds ---" % (time.time() - start_time))
