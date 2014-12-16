from node import Node 

class OrderedList:

    def __init__(self):

        self.head = None

    def add(self, item):

        n = Node(item)

        current = self.head
        
        previous = None
        stop = False
        
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            n.setNext(self.head)
            self.head = n
        else:
            n.setNext(current)
            previous.setNext(n)


    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()

        else:
            previous.setNext(current.getNext())

    def search(self, item):

        current = self.head

        while current:
            if current.getData() == item:
                return True
            elif current.getData() > item:
 
                return False
            current = current.getNext()

        return False

    def isEmpty(self):
        return self.head == None

    def length(self):
        current = self.head
        count = 0
        while current:
            current = current.getNext()
            count += 1
        return count


    def index(self, item):

        current = self.head
        count = 0

        while current:
            if current.getData() == item:
                return count
            else:
                current = current.getNext()
                count += 1
        return count

    def pop(self, pos=None):

        if self.isEmpty():
            return "Linked list is empty; nothing to pop."

        current = self.head
        previous = None

        if not pos:

            while current.getNext() != None:

                previous = current
                current = current.getNext()

            
            result = current.getData()

            if previous != None:
                previous.next = None
            else:
                current.setData = None
                current.setNext = None


            return result

        else:
            count = 0
            while pos > count:

                previous = current
                current = current.getNext()
                count += 1
                
            result = current.getData()

            if previous != None:
                previous.setNext(current.getNext())
            else:
                current.setData = None
                current.setNext = None

            
            return result



if __name__ == '__main__':
    link1 = OrderedList()
    link1.add(57)
    link1.add(5)
    print link1.index(5) # 0
    print link1.index(57)# 1
    print link1.pop(1) #57
    print link1.search(57) # False
    link1.add(6)
    link1.add(90)
    print link1.search(0) # False
    print link1.search(57) # False
    print link1.search(6) # True
    print link1.search(58) # False
    print link1.search(7) # False








            


