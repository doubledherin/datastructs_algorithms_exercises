from __future__ import division
from binaryTreeNodesAndReferences import BinaryTree 
from stack import Stack 

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
            currentTree.insertLeftChild('')
            parentStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif token in "*/+-":
            currentTree.setRootValue(token)
            currentTree.insertRightChild('')
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



