class SingleNode(object):
    """the node of single linked list"""

    def __init__(self, item):
        # _item save the values.
        self.item = item
        # _next is pointed the next node.
        self.next = None


class SingleLinkList(object):
    """Single linked list"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        """judge the linked list whether it is empty"""
        return self._head == None

    def length(self):
        """the length of linked list"""
        # cur point to head of list at start.
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """traverse the list"""
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print(" ")

    def add(self, item):
        """add a new element"""
        # create a new node to save the value
        node = SingleNode(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        """append a new element"""
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """insert a new element"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            pre = self._head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """remove a node"""
        cur = self._head
        pre = None
        while cur != None:
            if cur.item == item:
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """search the appointed node"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
