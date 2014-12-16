import time

def sumOfN(n):
    start = time.time()

    theSum = 0
    for i in range(1, n+1):
        theSum += i
    end = time.time()

    return theSum, end-start

def sumOfN2(n):
    start = time.time()

    sum = (n * (n+1))/2

    end = time.time()

    return sum, end-start

if __name__ == '__main__':
    for i in range(5):
        print "Sum is %d. Required %10.7f seconds." % sumOfN(100000)

    for i in range(5):
        print "Sum is %d. Required %10.7f seconds." % sumOfN2(100000)


