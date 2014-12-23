class BinaryTree:

    def __init__(self, rootObj):
        self.root = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, item):
        if self.leftChild == None:
            self.leftChild = BinaryTree(item)
        else:
            newNode = BinaryTree(item)
            newNode.leftChild = self.leftChild
            self.leftChild = newNode

    def insertRight(self, item):
        if self.rightChild == None:
            self.rightChild = BinaryTree(item)
        else:
            newNode = BinaryTree(item)
            newNode.rightChild = self.rightChild
            self.rightChild = newNode

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootValue(self, value):
        self.root = value

    def getRootValue(self):
        return self.root

def preorder(tree):
    if tree:
        print tree.getRootValue()
        preorder(tree.getLeftChild)
        preorder(tree.getRightChild)

def postorder(tree):
    if tree:
        postorder(tree.getLeftChild)
        postorder(tree.getRightChild)
        print tree.getRootValue()

def inorder(tree):
    if tree:
        inorder(tree.getLeftChild)
        print tree.getRootValue()
        inorder(tree.getRightChild)

if __name__ == '__main__':
    bt = BinaryTree(5)
    print bt
    bt.insertRight(6)
    bt.insertLeft(10)
    bt.insertRight(60)
    bt.insertLeft(100)
    bt.insertRight(65)
    bt.insertLeft(104)
    print bt.getRootValue()
    # preorder(bt)
    postorder(bt)




