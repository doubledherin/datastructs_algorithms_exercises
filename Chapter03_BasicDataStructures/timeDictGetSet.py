import timeit
import random


for i in range(10000, 1000001, 20000):

    d = {j:None for j in range(i)}
    
    t1 = timeit.Timer("d[random.randrange(%d)]" % i, 
                     "from __main__ import random, d")
    getter_time = t1.timeit(number=1000)

    t2 = timeit.Timer("d[random.randrange(%d)] = 0" % i, 
                      "from __main__ import random, d")
    setter_time = t2.timeit(number=1000)

    print("%d, get: %10.3f, set: %10.3f" % (i, getter_time, setter_time))

