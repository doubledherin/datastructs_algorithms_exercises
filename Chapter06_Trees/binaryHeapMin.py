class BinaryHeapMin():

    def __init__(self):
        self.heapList = [0]
        self.currentsize = 0

    def insert(self, k):
        self.heapList.append(k)
        self.currentsize = self.currentsize+1
        self.percUp(self.currentsize)

    def percUp(self, i):
        while i // 2 > 0:
            # Continually swap places with parent if item is smaller than parent
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i = i//2

    def findMin(self):
        return self.heapList[1]

    def delMin(self):
        # min is root
        min = self.heapList[1]
        # overwrite min with latest append
        self.heapList[1] = self.heapList[self.currentsize]
        # decrement size of heapList
        self.currentsize -= 1
        # remove duplicate item that is at top and bottom of heap
        self.heapList.pop()

        self.percDown(1)
        return min

    def percDown(self, i):
        while (i * 2) <= self.currentsize:
            indexMinChild = self.getIndexMinChild(i)
            if self.heapList[i] > self.heapList[indexMinChild]:
                self.heapList[i], self.heapList[indexMinChild] = self.heapList[indexMinChild], self.heapList[i]
            i = indexMinChild

    def getIndexMinChild(self, i):
        # if there's no right child
        if i * 2 + 1 > self.currentsize:
            return i * 2

        else:
            if self.heapList[i*2] < self.heapList[(i*2)+1]:
                return i*2
            else:
                return (i*2)+1


    def isEmpty(self):
        return self.currentsize == 0


    def size(self):
        return self.currentsize

    def buildHeap(self, alist):

        i = len(alist)//2
        
        self.currentsize = len(alist)

        # create copy of list and assign to heaplist with 0 at the 0th index
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i -= 1

if __name__ == '__main__':
    bhm = BinaryHeapMin()
    bhm.buildHeap([67,9,3,7,4,15,46])

    for i in range(1,bhm.size()+1):
        print "i: ", i, "; contents: ", bhm.heapList[i]
    print bhm.isEmpty() # False
    print bhm.findMin() #3
    print bhm.size() #7
    bhm.insert(1)
    print bhm.findMin() #1
    print bhm.size() #8
    bhm.delMin()
    print bhm.findMin() #3
    print bhm.size() #7
    print bhm.getIndexMinChild(3) #7
        


