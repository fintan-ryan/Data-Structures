from binaryheap import BinaryHeap, Node


class Element:
    def __init__(self, key, value):
        self._key = key
        self._value = value

    def __str__(self):
        print(str(self._key) + ' : ' + str(self._value))

    def __eq__(self, other):
        return self._key == other._key

    def __lt__(self, other):
        return self._key < other._key

    def to_string(self):
        return str(self._key) + ' : ' + str(self._value)


class APQ:
    def __init__(self):
        self._queue = BinaryHeap()

    def __str__(self):
        heap_items = [(i._element.to_string()) for i in self._queue._heap[1::] if i is not None]
        heap_items_str = ' -> '.join(heap_items)
        print(heap_items_str)

    def get_size(self):
        return self._queue.getSize()

    def add(self, k, v):
        temp_el = Element(k, v)
        self._queue.add(temp_el)

    def build_apq(self, temp_dict):
        temp_list = [Element(mydict[i], i) for i in temp_dict]
        return self._queue.heapHelper(temp_list)

    def min(self):
        return self._queue.getMin()

    def remove_min(self):
        # Some issues with __str__()
        return self._queue.removeMin()

    def get_parent(self,i):
        if (i-1)//2 == 0:
            return self._queue._heap[1]
        else:
            return self._queue.getParent(i)


    def update_key(self, element, newkey):
        for i in range(len(self._queue._heap[1::])+1):
            if self._queue._heap[i]._element:
                if self._queue._heap[i]._element._value == element:
                    self._queue._heap[i]._element._key = newkey
                    if self._queue._heap[i]._element < self.get_parent(i+1)._element:
                        self._queue.percUp(i)

                    else:
                        self._queue.percDown(i)

    def get_key(self, element):
        for i in range(len(self._queue._heap[1::]) + 1):
            if self._queue._heap[i]._element:
                # print(self._queue._heap[i]._element._value)
                if self._queue._heap[i]._element == element:
                    return self._queue._heap[i]._element._key

    def remove_element(self, element):
        for i in range(len(self._queue._heap[1::])+1):
            if self._queue._heap[i]._element:
                # print(self._queue._heap[i]._element._value)
                if self._queue._heap[i]._element._value == element:
                    removal = self._queue._heap[i]._element
                    self._queue.swap(i, 1)
                    self.remove_min()
                    # return key, value
                    return removal.__str__()


# APQ Testing
# print('Starting test')
# Creating our APQ
# animals = APQ()
# a2 = APQ()
# Creating information to store in our APQ
# mydict = {'bed':14, 'dog':22, 'ant':35, 'fox':18, 'egg':27, 'cat':24}

# animals.build_apq(mydict)
# print('animals')
# animals.__str__()

# animals.remove_min()
# print(animals.update_key(Element('dog',22), 'cocker spaniel'))
# animals.__str__()

# (animals._queue.getLeftChild(2)).__str__()

"""for i in ((mydict)):
    a2.add(mydict[i], i)"""

# a2.__str__()

# print(a2.remove_min())
# a2.__str__()

#print((animals._queue._heap).__str__())