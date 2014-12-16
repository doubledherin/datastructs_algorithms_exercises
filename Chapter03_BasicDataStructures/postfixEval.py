from stack import Stack 

def postfixEval(tokenString):
    operandStack = Stack()

    tokenList = list(tokenString)

    for token in tokenList:

        if token == " ":
            continue
        elif token.isdigit():
            operandStack.push(int(token))

        else:

            top = operandStack.pop()
            next = operandStack.pop()
            result = arithmetic(token, next, top)
            operandStack.push(result)

    return operandStack.pop()


def arithmetic(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2




if __name__ == '__main__':
    print postfixEval("4 5 6 * +")
    print postfixEval("7 8 + 3 2 + /")
