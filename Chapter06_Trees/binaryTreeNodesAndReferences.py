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

    def getRootValue(self, value):
        return self.root




