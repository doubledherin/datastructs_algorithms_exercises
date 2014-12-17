def baseConverter(num, base):
    """
    Takes an integer (base 10) and converts it to a string representation of that number in the indicated base (from 2 to 16, inclusive).
    """

    digits = "0123456789ABCDEF"

    if num < base:
        return digits[num]
    else:
        return baseConverter(num//2, base) + digits[num%base]

if __name__ == '__main__':
    print baseConverter(10, 2)