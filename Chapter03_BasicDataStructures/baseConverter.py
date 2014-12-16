from stack import Stack 

def baseConverter(number, base):
    """
    Takes a number and converts it to the provided base.
    """

    digits = "0123456789ABCDEF"

    remainders = Stack()

    while number > 0:
        rem = number % base
        remainders.push(rem)
        number = number // base

    result = ""

    while not remainders.isEmpty():
        popped = remainders.pop()
        digit = digits[popped]
        result += str(digit)
    return result

if __name__ == '__main__':
    

    number = input("Enter a number: ")
    base = input("Enter a base up to 16: ")

    print "The number %d in base %d is %s." % (number, base, baseConverter(number, base))