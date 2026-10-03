class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key, size):
        return key%size # 56 % 11 => 1

    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, self.size)

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:    # modify
                self.data[hashvalue] = data
            else:   # collision
                # nextslot 希望得知下一格要放哪裡 linear probing
                nextslot = self.rehash(hashvalue, self.size)
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(hashvalue, self.size)
                # nextslot 就是我們找到的格子
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace/modify

    def get(self, key):
        startslot = 

    def __setitem__(self, key, data):   # list: key->index , dict: key->key
        self.put(key, data)

    def __getitem__(self, key):
        return 0

if __name__ == '__main__':
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"

    print(H[54])

    print(H.slots)
    print(H.data)