import time
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
