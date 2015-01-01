class BinaryHeapMax:

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, item):
        self.heapList.append(item)
        self.currentSize +=1
        self.percUp(self.currentSize)

    def percUp(self, i):
        while i//2 > 0:
            if self.heapList[i] > self.heapList[i//2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i = i//2

    def percDown(self, i):
        while i*2 <= self.currentSize:
            indexMaxChild = self.getIndexMaxChild(i)
            if self.heapList[i] < self.heapList[indexMaxChild]:
                self.heapList[i], self.heapList[indexMaxChild] = self.heapList[indexMaxChild], self.heapList[i]
            i = indexMaxChild

    def getIndexMaxChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] > self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1


    def findMax(self):
        return self.heapList[1]

    def delMax(self):
        max = self.findMax()
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return max

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
    bhm = BinaryHeapMax()
    bhm.buildHeap([67,9,3,7,4,15,46])

    print bhm.heapList
    # for i in range(1,bhm.size()+1):
    #     print "i: ", i, "; contents: ", bhm.heapList[i]
    # print bhm.isEmpty() # False
    # print bhm.findMax() #3
    # print bhm.size() #7
    # bhm.insert(1)
    # print bhm.findMax() #1
    # print bhm.size() #8
    # bhm.delMin()
    # print bhm.findMax() #3
    # print bhm.size() #7
    # print bhm.getIndexMaxChild(3) #7
