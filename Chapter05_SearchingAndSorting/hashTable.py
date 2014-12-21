class HashTable:

    def __init__(self):
        self.size = 11 # or any prime number
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key):
        return key % (self.size)

    def rehash(self, oldhashvalue):
        return oldhashvalue+1% (self.size)

    def put(self, key, data):
        hashvalue = self.hashfunction(key)

        # If slot is empty, fill it. If slot already contains that key, replace data.
        if self.slots[hashvalue] == None or self.slots[hashvalue] == key:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data # replace

        # If slot is filled with a different key, compute next slot with rehash
        else:
            nextslot = self.rehash(hashvalue)

            # If the next slot is filled with anything other than the key, rehash
            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot)
            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot] = data
            else:
                self.data[nextslot] = data # replace

    # overload built-in to get access to [] syntax
    def __setitem__(self, key, data):
        self.put(key, data)

    def get(self, key):

        firstposition = self.hashfunction(key)
        
        data = None
        found = False
        tooFar = False

        position = firstposition

        while self.slots[position] != None and not found and not tooFar:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)

                if position == firstposition:
                    tooFar = True
        return data

    # overload built-in to get access to [] syntax
    def __getitem__(self, key):
        return self.get(key)





if __name__ == '__main__':
    h = HashTable()
    hashvalue = h.hashfunction(50) 
    print hashvalue #6
    hashvalue2 = h.hashfunction(61) 
    print hashvalue2 #6
    hashvalue3 = h.rehash(hashvalue2)
    print hashvalue3 #7
    h[50] = "cat"
    print h.data[6] # cat
    print h[50] # cat