class Node:

    def __init__(self, value):
        self.value = value
        self.nxt = None
        self.pre = None


class LinkedList:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def add(self, idx, element):
        if idx < 0 or idx > self.size:
            return

        if idx == 0:
            return self.add_first(element)

        if idx == self.size:
            return self.add_last(element)

        nxt_node = self.get(idx)
        pre_node = nxt_node.pre

        new_node = Node(element)
        new_node.nxt = nxt_node
        new_node.pre = pre_node

        nxt_node.pre = new_node
        pre_node.nxt = new_node
        self.size += 1
        return new_node

    def add_first(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return new_node

        new_node.nxt = self.head
        self.head.pre = new_node

        self.head = new_node
        self.size += 1
        return new_node

    def add_last(self, element):
        new_node = Node(element)
        if self.tail is None:
            return self.add_first(element)
        new_node.pre = self.tail
        self.tail.nxt = new_node
        self.tail = new_node
        self.size += 1
        return new_node

    def remove(self, idx):
        if idx < 0 or idx >= self.size:
            return

        if self.size == 0:
            return

        if idx == 0:
            return self.remove_first()

        if idx == self.size - 1:
            return self.remove_last()

        remove_node = self.get(idx)
        pre_node = remove_node.pre
        nxt_node = remove_node.nxt

        pre_node.nxt = nxt_node
        nxt_node.pre = pre_node
        self.size -= 1

        return remove_node

    def remove_first(self):
        remove_node = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return remove_node
        nxt_node = remove_node.nxt
        nxt_node.pre = None
        self.head = nxt_node
        self.size -= 1
        return remove_node

    def remove_last(self):
        remove_node = self.tail
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return remove_node
        pre_node = remove_node.pre
        pre_node.nxt = None
        self.tail = pre_node
        self.size -= 1
        return remove_node

    def get(self, idx):
        if idx < 0 or idx >= self.size:
            return

        return_node = self.head

        for _ in range(idx):
            return_node = return_node.nxt

        return return_node
