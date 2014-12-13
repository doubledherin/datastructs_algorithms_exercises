from stack import Stack 

def convertDecToBin(dec):
    """
    Takes a base 10 number and returns it in base 2.
    """

    remainders = Stack()

    while dec > 0:
        rem = dec % 2
        remainders.push(rem)
        dec = dec // 2

    result = ""

    while not remainders.isEmpty():
        result += str(remainders.pop())

    return int(result)


if __name__ == '__main__':
    

    entry = input("Enter a base 10 integer to convert to binary: ")

    print "The binary version of %d is %d." % (entry, convertDecToBin(entry))