class Heap(object):

    def __init__(self, k = 2):
        self._H = [0]
        self._size = 0
        self._allocation = 1
        self._k = k

    def getSize(self):
        return self._size

    def getAllocation(self):
        return self._allocation

    def getArray(self):
        return self._H

    def parent(self, pos):
        if pos <=0: return None
        else: return ((pos-1)-(pos-1)%self._k)/self._k

    def swap(self,pos1,pos2):
        s = self.getSize()
        if 0 <= pos1 and 0 <= pos2 and pos1 < s and pos2 < s:
            self._H[pos1], self._H[pos2] = self._H[pos2], self._H[pos1]

    def insert(self, item):
        if self._size == self._allocation:
            self._H = self._H[:]+[0]*self._allocation
            self._allocation = self._allocation * 2

        self._H[self._size] = item
        pos = self._size
        self._size += 1

        while pos > 0 and self._H[self.parent(pos)] > self._H[pos]:
            self.swap(self.parent(pos),pos)
            pos = self.parent(pos)

    # Return the index of child number i of the node at position pos.
    # Preconditions are that pos is a valid index. It will return
    # the index of this child, whether or not it exists and whether
    # or not its position is beyond the end of the heap array
    def childIndex(self, pos, i):
        
        return  pos * self._k + 1 + i
    
    # Tell the key in child number i (i in 0,1) of the node at position 'pos'
    # of heap array. If there is no such child, return None. Precondition
    # is that i is in {0,1}
    def child (self, pos, i):
        cIndex = self.childIndex(pos, i)
        if cIndex > self._size - 1 or self._H[cIndex] == None:
            return None
        else: return self._H[cIndex]


    """
    Return a list of keys at children of the node at position pos.
    Return None if 'pos' is not in {0, 1, 2, ... size-1}
    If it is, it might have 2, 1 or 0 children; return a list of length 2, 1
    or 0.
    Here's a hint: create a list of self.child(pos,i) for i in
    [leftChild, leftChild+1]. One or both of these could be None,
    indicating the child doesn't exist. Create and return a new
    list that is equal to this list, but with the None values omitted.
    """

    def children(self, pos):
        _children = []
        if pos < 0 or pos > self._size - 1:
            return None
        else:
            for i in range(self._k):
                if self.child(pos, i) != None:
                    _children.append(self.child(pos, i))
            return _children

    # Extract the minimum element of the heap, and restore the heap property.
    # See our book for the algorithm.
    def extractMin(self):
        extracted = self._H[0]
        self._H[0] = self._H[self._size]
        self._size = self._size - 1
        currentPos = 0
        self.heapify(currentPos)
        return extracted

    """
    In a subtree rooted at pos in which the only place where the heap
    property does not apply is at the root, restore the heap property.
    A precondition is that 0 <= pos < self._size.
    Here's a hint: call self.children(pos). If the returned list C
    is empty, the element at 'pos' has no children, and the heap
    property applies. Otherwise, if min(C) > self._H(pos),
    the heap property applies. Otherwise, you can find which child
    number contains the minimum key with childNum = C.index(min(C)). (Look
    up this 'index' method.) You can tell the index of this child
    in self._H with a call to self.childIndex(pos, childNum).
    """
    def heapify(self, pos):
        currentPos = pos
        while True:
            if len(self.children(currentPos)) != 0:
                minchild = min(self.children(currentPos))
                if self._H[currentPos] > minchild:
                    self.swap(currentPos, self.children.index(minchild))
                else: break
            else: break                      
        pass
                              
    """
    Create a string that is suitable for displaying structure of the heap
    To print the heap array, print P._H. This one displays which key
    is a child of which using indentation. For example:
    3
     5
      10
      29
     4
      20
      15
    The least indented element, 3, is at the root. Its children
    are the elements 5 and 4 at the next level of indentation.
    The two elements at the next level of indentation following 5,
    namely, 10 and 29, are the children of 5. Similarly, 20 and 15
    are the children of 4.
    """

    """
    I've commented it out because it won't work until you've written
    some of your methods ...
    """

    
    def __str__(self):
        if self.getSize() == 0: return ""
        else: return self.strAux(0, 0, "")

    def strAux(self, pos, depth, outString):
        outString = outString + "\n" + ' ' * depth + str(self._H[pos])
        children = self.children(pos)
        for i in range(len(children)):
            outString = self.strAux(self.childIndex(pos,i), depth+1, outString)
        return outString
    

    
if __name__ == "__main__":
    P = Heap()
    P.insert(10)
    P.insert(5)
    P.insert(15)
    P.insert(3)
    P.insert(29)
    print "Heap array: " + str(P.getArray())
    print "Size: " + str(P.getSize())
    print "allocation " + str(P.getAllocation())
    # This will print the structure of the heap once you've written
    # your other methods, because of the __str__ method I've written
    print P

    # This is the test for 3-ary Heap. Not sure I can change main function or not.
    # So I have commented it out.
    """
    Q = Heap(3)
    Q.insert(10)
    Q.insert(3) 
    Q.insert(7)
    Q.insert(9)
    Q.insert(8)
    Q.insert(15)
    Q.insert(20)
    Q.insert(17)
    print "Heap array: " + str(Q.getArray())
    print "Size: " + str(Q.getSize())
    print "allocation " + str(Q.getAllocation())
    print Q
    """
