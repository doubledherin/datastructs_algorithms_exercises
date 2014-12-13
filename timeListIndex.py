import timeit
import random


for i in range(10000, 1000001, 20000):
    t = timeit.Timer("x[random.randrange(%d)]" % i, 
                     "from __main__ import random, x")
    x = list(range(i))
    index_time = t.timeit(number=1000)


    print("%d, list: %10.3f" % (i, index_time))

