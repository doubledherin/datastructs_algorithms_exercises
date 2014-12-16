from node import Node 

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        n = Node(item)
        n.setNext(self.head)
        self.head = n

    def length(self):

        count = 0

        current = self.head

        while current:
            current = current.getNext()
            count +=1

        return count

    def search(self, item):

        current = self.head
        found = False
        while current and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

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

    def append(self, item):
        """
        Adds a new item to the end of the list, making it the last item in the collection.
        """
        n = Node(item)
        current = self.head

        while current.getNext() != None:
            current = current.getNext()

        current.setNext(n)

    def insert(self, position, item):
        
        n = Node(item)


        current = self.head
        previous = None

        for i in range(position):
            previous = current
            current = current.getNext()

        if previous == None:

            n.setNext(current)
            self.head = n

        else:
            n.setNext(current)
            previous.setNext(n)

        return

    def index(self, item):

        count = 0
        found = False
        current = self.head

        while not found and current.getNext():
            if current.getData() == item:
                found = True

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
    link1 = UnorderedList()
    link2 = UnorderedList()

    link1.add(1)
    link1.add(2)
    link1.add(3)
    print link1.isEmpty()
    print link2.isEmpty()

    print link1.length()
    print link2.length()
    print link1.search(3)
    print link2.search(3)
    link1.remove(3)
    print link1.search(3)
    link1.append(3)
    print link1.search(3)
    link1.insert(1, "apple")
    print link1.index("apple")
    print link1.pop(2)
    print link1.pop()




















                
