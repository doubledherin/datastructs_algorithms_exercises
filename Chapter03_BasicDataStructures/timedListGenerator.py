from timeit import Timer

def test1():
    l = []
    for i in range(1000):
        l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

def test5():
    """
    Adding empty function to see how much time it takes just to call a function.
    """
    pass

t1 = Timer("test1()", "from __main__ import test1")
print ("concat ", t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print ("append ", t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print ("comprehension ", t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print ("range ", t4.timeit(number=1000), "milliseconds")
t5 = Timer("test5()", "from __main__ import test5")
print ("empty ", t5.timeit(number=1000), "milliseconds")