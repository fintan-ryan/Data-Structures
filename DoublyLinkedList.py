class DLLNode:
    def __init__(self, val, last, next):
        self.val = val
        self.next = next
        self.prev = last

class DLL:
    def __init__(self):
        self.head = DLLNode(None, None, None)
        self.tail = DLLNode(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head # List loops around
        self.length = 0

    def add_node(self, item):
        node = self.head
        newNode = DLLNode(item, node, node.next)
        node.next = newNode
        self.tail.prev = newNode
        self.length += 1

    def add_after(self, item, before):
        node = self.head
        while node != before:
            node = node.next
        print(node.next)
        newNode = DLLNode(item, node, node.next)
        node.next.prev = newNode
        self.length += 1

    def add_first(self, item):
        self.add_after(item, self.head)

    def add_last(self, item):
        self.add_after(item, self.tail)

    def get_first(self):
        return self.head.next

    def get_last(self):
        return self.tail.prev


    def remove_node(self, node):
        node.prev.next = node.next

    def remove_first(self):
        self.remove_node(self.get_first())

    def remove_last(self):
        self.remove_node(self.get_last())

    def __str__(self):
        playlist = '['
        node = self.head
        while node != self.tail:
            playlist += str(node)
            node = node.next
            # playlist += str(node.val)
        return playlist

    def to_list(self):
        ret_list = []
        current = self.head.next
        while current != None:
            ret_list.append(str(current.val))
        return ret_list
