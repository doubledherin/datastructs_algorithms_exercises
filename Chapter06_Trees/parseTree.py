from __future__ import division
import operator
from binaryTreeNodesAndReferences import BinaryTree, preorder, postorder 
from stack import Stack 

add = operator.add
sub = operator.sub
mul = operator.mul
div = operator.truediv

def parseTree(expression):
    """
    Takes a string, returns a number.

    Takes a fully parenthesized mathematical expression and
    uses a binary parse tree to evaluate it.
    """

    # split expression into list of tokens
    expressionList = list(expression)

    # remove empty strings
    for token in expressionList:
        if token == ' ':
            expressionList.remove(token)

    parentStack = Stack()
    
    parseTree = BinaryTree('')

    parentStack.push(parseTree)

    currentTree = parseTree

    for token in expressionList:
        if token == "(":
            currentTree.insertLeft('')
            parentStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif token in "*/+-":
            currentTree.setRootValue(token)
            currentTree.insertRight('')
            parentStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif token not in "*/+-)":
            currentTree.setRootValue(eval(token))
            currentTree = parentStack.pop()

        elif token == ")":
            currentTree = parentStack.pop()

        else:
            raise ValueError("Unknown operator: " + i)

    return parseTree


def evaluate(parseTree):

    # create dict of operators
    # key = string version, val = python's built-in operator equivalent
    opers = {'+': add, '-': sub, '*': mul, '/': div}
    leftChild = parseTree.getLeftChild()
    rightChild = parseTree.getRightChild()

    # not at leaf nodes yet
    if leftChild and rightChild:
        operator = opers[parseTree.getRootValue()]
        return operator(evaluate(leftChild), evaluate(rightChild))

    # at leaf nodes now
    else:
        return parseTree.getRootValue()

if __name__ == '__main__':
    pTree = parseTree('(3 + (4 * 5))')
    print evaluate(pTree) #23



