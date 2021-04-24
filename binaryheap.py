class Node:
    def __init__(self, element):
        self._element = element

    def __str__(self):
        print(str(self._element))

    def __eq__(self, other):
        return self._element == other._element

    def __lt__(self, other):
        return self._element < other._element

    # This may be redundant
    def get_element(self):
        return self._element


class BinaryHeap:
    def __init__(self):
        head_node = Node(0)
        self._heap = [head_node]
        self._size = 0

    def __str__(self):
        # method a
        """
        for i in self._heap[1::]:
            print(i._element)
        """
        # method b
        """
        for i in range(1, (self._size // 2) + 1):
            if self._heap[i] is None or self._heap[2*i] is None or self._heap[2*i+1] is None:
                continue
            else:
                print("parent : " + str(self._heap[i]._element) + " left child : " +
                      str(self._heap[2 * i]._element) + " right child : " +
                      str(self._heap[2 * i + 1]._element))
        """

        # method c
        """
        for i in range(1, (self._size // 2) + 1):
            print("parent : " + str(self._heap[i]._element) + " left child : " +
                      str(self._heap[2 * i]._element) + " right child : " +
                      str(self._heap[2 * i + 1]._element))
        """
        # method d
        """for i in range(1, (self._size // 2) + 1):
            outstr = '['
            if self.getLeftChild(i) is not None:
                outstr = outstr + "left: " + str(self.getLeftChild(i)._element)
            else:
                outstr = outstr + 'left: *'
            if self.getRightChild(i) is not None:
                outstr = outstr + "; right: " + str(self.getRightChild(i)._element) + ']'
            else:
                outstr = outstr + '; right: *]'
            if self.getParent(i) is not None:
                outstr = outstr + ' -- parent: ' + str(self.getParent(i)._element)
            else:
                outstr = outstr + ' -- parent: *'
            print(outstr)
            if self.getLeftChild(i) is not None:
                self.getLeftChild(i).__str__()
            if self.getRightChild(i) is not None:
                self.getRightChild(i).__str__()"""
        # method e
        """
        ret = '['
        for i in self._heap[1::]:
            ret += (str(i)) + '->'
        ret = ret[:-2] + ']'
        print(ret)
        """
        # method f
        if self._size > 0:
            """for i in self._heap:
                print((str(i._element)))"""
        heap_items = [str(i._element) for i in self._heap[1::] if i]
        heap_items_str = ' -> '.join(heap_items)
        print(heap_items_str)

    def heapHelper(self, input_list):
        temp_list = [Node(i) for i in input_list]
        head_node = Node(0)
        i = len(temp_list) // 2
        self._size = len(temp_list)
        self._heap = [head_node] + temp_list[:]
        while i > 0:
            self.percDown(i)
            i -= 1

    def percUp(self, i):
        while i // 2 > 0:
            if self._heap[i] < self._heap[i//2]:
                # mehtod a.
                # print(self._heap[i], self._heap[i//2])
                # self._heap[i], self._heap[i//2] = self._heap[i//2], self._heap[i]
                # print(self._heap[i], self._heap[i // 2])

                # method b.
                self.swap(i, i//2)
            i = i//2

    def percDown(self, i):
        while i * 2 <= self._size:
            temp_min = self.getMinChild(i)
            if self._heap[i] > self._heap[temp_min]:
                # method a.
                # self._heap[i], self._heap[temp_min] = self._heap[temp_min], self._heap[i]

                # method b.
                self.swap(i, temp_min)
            i = temp_min

    def swap(self, a, b):
        self._heap[a], self._heap[b] = self._heap[b], self._heap[a]

    def getMin(self):
        if self._size > 0:
            return self._heap[1]
        else:
            return None

    def getMinChild(self, i):
        if i * 2 + 1 > self._size:
            return i * 2
        else:
            if self._heap[i*2] < self._heap[i*2+1]:
                return i*2
            else:
                return i*2+1

    def removeMin(self):
        removing = self._heap[1]
        self._heap[1] = self._heap[self._size]
        self._size = self._size - 1
        self._heap.pop()
        self.percDown(1)
        return removing._element

    def add(self, item):
        temp_node = Node(item)
        # print(type(temp_node._element))
        # (temp_node.__str__())
        # if self._size > 0:
        # method a.
        """
        for node in self._heap[1::]:
            if temp_node == node:
                print(str(item) + ' has already been added')
        """
        # method b.
        """
        if temp_node in self._heap[1::]:
            print('duplicate found')
            print(item.__str__())
            # print(str(temp_node.__str__()) + ' has already been added')

        else:
            self._heap.append(temp_node)
            self._size += 1
            self.percUp(self.getSize())
            temp_node._element.__str__()
    else:
        self._heap.append(temp_node)
        self._size += 1
        self.percUp(self.getSize())
        temp_node._element.__str__()
        """
        # method c.
        self._heap.append(temp_node)
        self._size += 1
        self.percUp(self.getSize())
        temp_node._element.__str__()

    def getSize(self):
        return self._size

    def getParent(self, i):
        return self._heap[(i-1)//2]

    def getLeftChild(self, i):
        return self._heap[2*i+1]

    def getRightChild(self, i):
        return self._heap[2*i+2]


# Binary Heap Testing

bh1 = BinaryHeap()
# bh1.add(1)
# bh1.__str__()
# bh1.add(2)
example_input = [1, 3, 5, 2, 4, 7, 9, 35, 23, 11, 25]
"""for i in example_input:
    bh1.add(i)

bh1.__str__()
bh1.removeMin()
bh1.__str__()"""


#print(bh1.__str__())
"""print(bh1.__str__())
bh1.removeMin()
print(bh1.__str__())
# print(bh1.getMin())
(bh1.removeMin())
print(bh1.__str__())"""

class Crazy:
    def __init__(self, element):
        self._element = element

    def __str__(self):
        print(str(self._element))


# c1 = Crazy(2)
# n1 = Node(.2)
# n1.__str__()
# c1.__str__()

# n2 = Node(c1)
# print(str(n2._element._element))

