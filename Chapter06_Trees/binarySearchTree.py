class TreeNode:

    def __init__(self, key, value, left=None, right=None, parent=None):

        self.key = key
        self.payload = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self == self.parent.leftChild

    def isRightChild(self):
        return self.parent and self == self.parent.rightChild

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not self.leftChild and not self.rightChild

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, value, leftChild, rightChild):
        self.key = key
        self.payload = value
        self.leftChild = leftChild
        self.rightChild = rightChild
        if self.hasRightChild:
            self.rightChild.parent = self
        if self.hasLeftChild:
            self.leftChild.parent = self

    def findSuccessor(self):
        successor = None
        if self.hasRightChild():
            successor = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    successor = self.parent
                else:
                    self.parent.rightChild = None
                    successor = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return successor

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                   self.parent.leftChild = None
            else:
                   self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                   if self.isLeftChild():
                      self.parent.leftChild = self.leftChild
                   else:
                      self.parent.rightChild = self.leftChild
                   self.leftChild.parent = self.parent
            else:
                   if self.isLeftChild():
                      self.parent.leftChild = self.rightChild
                   else:
                      self.parent.rightChild = self.rightChild
                   self.rightChild.parent = self.parent

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for item in self.leftChild:
                    yield item
            yield self.key
            if self.hasRightChild():
                for item in self.rightChild:
                    yield item





class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.length()

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _put(self, key, value, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, value, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, value, parent=currentNode)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.payload
            else:
                return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error: that key is not in the tree.')

        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1

        else: 
            raise KeyError('Error: that key is not in the tree.')

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            successor = currentNode.findSuccessor()
            successor.spliceOut()
            currentNode.key = successor.key
            currentNode.payload = successor.payload
        else:
            # current node has only one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    # and current node is root
                    currentNode.replaceNodeData(currentNode.leftChild.key, currentNode.leftChild.payload, currentNode.leftChild.leftChild, currentNode.leftChild.rightChild)
            else:
                # current node has only a right child
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key, currentNode.rightChild.payload, currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst[3] = "Oakland"
    bst[4] = "San Francisco"
    bst[6] = "Yreka"
    bst[2] = "Concord"

    print bst.length() #4
    print len(bst) #4
    bst.put(1, "Berkeley")
    print bst.length() #5
    print len(bst) #5
    print bst.get(1) #"Berkeley"
    print 6 in bst # True
    print 8 in bst # False
    bst.delete(2)
    print bst.length() #4
    print len(bst) #4
    for item in bst:
        print item, bst.get(item)



