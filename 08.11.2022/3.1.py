import random
import time
start_time = time.time()
x = random.randint(0, 100)
print(f'x: {x}', x**5)
print("--- %s seconds ---" % (time.time() - start_time))
