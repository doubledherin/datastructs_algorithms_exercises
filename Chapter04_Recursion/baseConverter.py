from stack import Stack

stacky = Stack()

def baseConverter1(num, base):
    """
    Using recursion, takes an integer (base 10) and converts it to a string representation of that number in the indicated base (from 2 to 16, inclusive).
    """

    digits = "0123456789ABCDEF"

    if num < base:
        return digits[num]
    else:
        return baseConverter1(num//2, base) + digits[num%base]


def baseConverter2(num, base):
    """
    Using a stack and recursion, takes an integer (base 10) and converts it to that number in the indicated base (from 2 to 16, inclusive).
    """


    digits = "0123456789ABCDEF"

    if num < base:
        stacky.push(digits[num])
    else:
        stacky.push(digits[num%base])
        return baseConverter2(num//base, base) 

    result = ""
    while not stacky.isEmpty():
        toAdd = stacky.pop()
        result += toAdd
    return result




if __name__ == '__main__':
    # print baseConverter1(10, 2)
    print baseConverter2(10, 2)