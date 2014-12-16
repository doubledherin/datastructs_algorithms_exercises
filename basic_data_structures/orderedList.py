from node import Node 

class OrderedList:

    def __init__(self):

        self.head = None

    def add(self, item):
        n = Node(item)
        
        if self.isEmpty():
            self.head = n

        # if the added item is less than anything in the list
        elif self.head >= item:
            n.setNext(self.head)
            self.head = n

        else:
            current = self.head
            previous = None

            while current:

                # if the added item is greater than anything in the list
                if current.getNext() == None:
                    current.setNext(n)
                    break

                elif current.getData() <= item and current.getNext() >= item:
                    n.setNext(current.getNext())
                    current.setNext(n)
                else:
                    current = current.getNext()



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
    print link1.index(5) # 1
    print link1.index(57)# 0
    print link1.pop(1) #5
    print link1.search(57) # True
    link1.add(6)
    link1.remove(6)
    print link1.length() # 1
    print link1.isEmpty() # False
    print link1.pop() #57
    print link1.isEmpty() # True





            


