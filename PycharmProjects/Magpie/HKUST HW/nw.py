import random
import numpy as np
import time
N = [i+1 for i in range(10)]
average = []
for i in N:
    count_all = []
    start_time = time.time()
    # for j in range(20000):
    while (time.time() - start_time) < 0.1:
        con = False
        count = 0
        prize_lst = []
        while not con:
            if len(prize_lst) == i:
                con = True
            else:
                new = random.randint(1, 10)
                if new not in prize_lst:
                    prize_lst.append(new)
                count += 1
        count_all.append(count)
    average.append(round(np.mean(count_all),0))

template = '{:>3}\t\t{:<5}'
index = 1
print(template.format('N','Average boxes'))
for i in average:
    print(template.format(index, i))
    index += 1