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

        n = self.head

        while n:
            n = n.getNext()
            count +=1

        return count

    def search(self, item):

        current = self.head

        while current:
            if current.getData() == item:
                return True
            current = current.getNext()

        return False

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

    def append(self, linkedList):

        current = linkedList.head

        while current.getNext() != None:
            current = current.getNext()

        current.setNext(self.head)
        self.head = linkedList.head

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

    def index(self, item):

        count = 0
        found = False
        current = self.head

        while not found:
            if current.getData() == item:
                found = True

            else:
                current = current.getNext()
                count += 1

        return count

    def pop(self, item):

        if self.isEmpty():
            return "Linked list is empty; nothing to pop."

        current = self.head
        previous = None


        while current.getNext() != None:

            previous = current
            current = current.getNext()

        
        result = current.getData()
        if previous != None:
            previous.next = None

        return result

if __name__ == '__main__':
    link1 = UnorderedList()
    link2 = UnorderedList()
    link1.add(1)
    link1.add(2)
    link1.add(3)
    link2.add("a")
    link2.add("b")
    link2.add("c")
    link1.append(link2)
    link1.insert(0, "apple")
    print link1.pop()











                
