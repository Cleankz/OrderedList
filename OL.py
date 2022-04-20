from tkinter.font import names
import string


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 == v2:
            return 0
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2

    def add(self, value):
        n = Node(value)
        n.value = value
        node = self.head
        if self.head is not None and self.__ascending == True:
            while node != None:
                if node == self.head and node.value >= value:
                    n.next = node
                    node.prev = n
                    self.head = n
                    break
                if node == self.tail and node.value >= value:
                    prev = node.prev
                    n.next = node
                    n.prev = node.prev
                    node.prev = n
                    prev.next = n
                    break
                if node == self.tail and node.value < value:
                    node.next = n
                    n.prev = node
                    self.tail = n
                    break
                if node.value >= value:
                    prev = node.prev
                    n.next = node
                    n.prev = node.prev
                    node.prev = n
                    prev.next = n
                    break
                node = node.next
        if self.head is not None and self.__ascending == False:
            while node != None:
                if node == self.head and node.value <= value:
                    n.next = node
                    node.prev = n
                    self.head = n
                    break
                if node == self.tail and node.value <= value:
                    prev = node.prev
                    n.next = node
                    n.prev = node.prev
                    node.prev = n
                    prev.next = n
                    break
                if node == self.tail and node.value > value:
                    node.next = n
                    n.prev = node
                    self.tail = n
                    break
                if node.value <= value:
                    prev = node.prev
                    n.next = node
                    n.prev = node.prev
                    node.prev = n
                    prev.next = n
                    break
                node = node.next
        if self.head is None:
            self.head = n
            self.tail = n
            n.prev = None
            n.next = None
        # автоматическая вставка value
        # в нужную позицию



    def find(self, val, stop = False):
        node = self.head
        if stop == False:
            while node is not None:
                if node.value == val:
                    return node
                node = node.next
        else:
            while node is not None:
                if node.value > val and self.__ascending == True:
                    return node
                if node.value < val and self.__ascending == False:
                    return node
                if node.value == val:
                    return node
                node = node.next
        return None # здесь будет ваш код

    def delete(self, val):
        node = self.head
        while node is not None:
            if node.value == val and node == self.head and node == self.tail:
                node.next = None
                node.prev = None
                node.value = None
                node = None
                self.head = None
                self.tail = None
                break
            if node.value == val and node == self.head:
                self.head = node.next
                node.next = None
                node.value = None
                node = None
                node = self.head
                node.prev = None
                break
            if node.value == val and node == self.tail:
                self.tail = prev_node
                node.prev = None
                node.value = None
                node = None
                prev_node.next = None
                break
            if node.value == val:
                prev_node.next = node.next
                node.next = None
                node.prev = None
                node.value = None
                node = None
                node = prev_node.next
                node.prev = prev_node
                break
            prev_node = node
            node = node.next

    def clean(self, asc):
        self.__ascending = asc
        node = self.head
        self.head = None
        self.tail = None
        while node is not None:
            del_node = node
            node = node.next
            del_node.prev = None
            del_node.next = None
            del_node = None
        pass # здесь будет ваш код

    def len(self):
        L = 0
        node = self.head
        while node is not None:
            L += 1
            node = node.next
        return L # здесь будет ваш код

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if len(string.strip(v1,' ')) == len(string.strip(v2,' ')):
            return 0
        if len(string.strip(v1,' ')) < len(string.strip(v2,' ')):
            return -1
        if len(string.strip(v1,' ')) > len(string.strip(v2,' ')):
            return 1
        return 0