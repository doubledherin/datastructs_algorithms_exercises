def BinaryTree(root):
    return [root, [], []]

def insertLeft(root, newBranch):
    poppedLeftChild = root.pop(1)

    if len(poppedLeftChild) != []:
        root.insert(1, [newBranch, poppedLeftChild, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

def insertRight(root, newBranch):
    poppedRightChild = root.pop(2)

    if len(poppedRightChild) != []:
        root.insert(2, [newBranch, [], poppedRightChild])
    else:
        root.insert(2, [newBranch, [], []])
    return root