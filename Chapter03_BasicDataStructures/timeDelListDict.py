"""
Compares the time performance of the 'del' operator on lists and dictionaries.
"""

import timeit
import random


for i in range(10000, 110001, 20000):
    # start list version THIS WORKS
    r = random.randrange(i)
    
    t1 = timeit.Timer("del x[r]", 
                     "from __main__ import random, x, r")

    x = list(range(i))

    num = x[r]

    lst_time = t1.timeit(number=1000)

    x[r] = num


    # start dictionary version--STILL BROKEN; key error for some reason
    r = random.randrange(i)
    print 0
    t2 = timeit.Timer("del x[r]", 
                     "from __main__ import random, x, r")
    print 1
    x = {j:None for j in range(i)}

    print 2
    dict_time = t2.timeit(number=1000)

    print 3

    x[r] = None

    print("%d, list: %10.3f, dict: %10.3f" % (i, lst_time, dict_time))

