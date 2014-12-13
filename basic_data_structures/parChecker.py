from stack import Stack

def parChecker(s):
    """
    Takes a string of parentheses and returns True if they are balanced; False if not
    """

    m = Stack()

    for char in s:
        if char in "([{":
            m.push(char)
        else:
            if m.isEmpty():
                return False
            else:
                top = m.pop()
                if not match(top, char):
                    return False

    return m.isEmpty()

def match(char1, char2):
    openers = "([{"
    closers = ")]}"
    return openers.index(char1) == closers.index(char2)


print parChecker("({[[]]})({})([])")   # True
print parChecker("(({}])()()))")       # False
print parChecker("(()()(]")            # False