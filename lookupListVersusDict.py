import timeit
import random

for i in range(10000, 100001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" % i, 
                     "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)

    x = {j:None for j in range(i)}
    dict_time = t.timeit(number=1000)

    print("%d, list: %10.3f, dict: %10.3f" % (i, lst_time, dict_time))
