from stack import Stack

def parChecker(s):
    """
    Takes a string of parentheses and returns True if they are balanced; False if not
    """

    m = Stack()

    for char in s:
        if char == "(":
            m.push(char)
        else:
            if m.isEmpty():
                return False
            else:
                m.pop()

    return m.isEmpty()

print parChecker("(()()())")   # True
print parChecker("(()()()))")  # False
print parChecker("(()()()")    # False