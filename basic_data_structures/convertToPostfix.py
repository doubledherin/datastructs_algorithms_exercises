from stack import Stack 
import string

def convertToPostfix(tokenstring):
    """
    Takes a string of tokens making up an infix operation (parens, operands, and operators)and converts it to postfix notation.
    """

    precidence = {}
    precidence["*"] = 3
    precidence["/"] = 3
    precidence["+"] = 2
    precidence["-"] = 2
    precidence["("] = 1

    opstack = Stack()
    output = []

    tokenlist = list(tokenstring)

    for item in tokenlist:
        if item == ' ':
            tokenlist.remove(item)


    for token in tokenlist:
        if token in string.uppercase:
            output.append(token)

        elif token == "(":
            opstack.push(token)
        
        elif token == ")":
            popped = opstack.pop()
            while popped != "(":
                output.append(popped)
                popped = opstack.pop()
        
        else:
            while (not opstack.isEmpty()) and (precidence[token] <= precidence[opstack.peek()]):
                
                output.append(opstack.pop())
            opstack.push(token)

    while not opstack.isEmpty():
        output.append(opstack.pop())

    return " ".join(output)


if __name__ == '__main__':
    print convertToPostfix("(A + B) * (C + D)")
    print convertToPostfix("(A + B) * C")
    print convertToPostfix("A + B * C")