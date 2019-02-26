from __future__ import print_function
import argparse

class Node:
    def __init__(self, data_='', next_=None):
        self.data = data_
        self.next = next_

class DLLNode:
    def __init__(self, data_='', next_=None, prev_=None):
        self.data = data_
        self.next = next_
        self.prev = prev_

class LinkedList:
    def __init__(self, front_=None):
        self.front = front_
    
    def __len__(self):
        curr = self.front
        cntr = 0
        while curr != None:
            cntr += 1
            curr = curr.next
        return cntr
    
    def __str__(self):
        if self.front == None:
            return 'empty list'
        str_list = [str(self.front.data)]
        curr = self.front.next
        while curr != None:
            str_list.append(' -> ')
            str_list.append(str(curr.data))
            curr = curr.next
        return ''.join(str_list)
    
    def __repr__(self):
        return 'LinkedList: ' + self.__str__()

    def addBefore(self, target_, newItem_):
        prev = None
        curr = self.front
        while curr != None and curr.data != target_:
            prev = curr
            curr = curr.next
        if curr == None:
            return self.front
        newNode = Node(newItem_, curr)
        if prev == None:
            self.front = newNode
        else:
            prev.next = newNode
        return self.front
    
    def append(self, newItem):
        newNode = Node(newItem, None)
        prev = None
        curr = self.front
        while curr != None:
            prev = curr
            curr = curr.next
        if prev == None:
            self.front = newNode
        else:
            prev.next = newNode

class CircularLinkedList:
    def __init__(self, rear_):
        self.rear = rear_
    
    def __len__(self):
        """
        start from front
        """
        # if self.rear == None:
        #     return 0
        # curr = self.rear.next  # curr at first
        # prev = self.rear
        # cntr = 0
        # while True:
        #     cntr += 1
        #     prev = curr
        #     curr = curr.next
        #     if prev == self.rear:
        #         break
        # return cntr

        """
        start from rear
        """
        if self.rear == None:
            return 0
        cntr = 0
        curr = self.rear
        while True:
            cntr += 1
            curr = curr.next
            if curr == self.rear:
                break
        return cntr
    
    def __str__(self):
        if self.rear == None:
            return 'empty list'
        curr = self.rear.next  # curr at first
        prev = self.rear
        str_list = []
        while True:
            str_list.append(str(curr.data))
            str_list.append(' -> ')
            prev = curr
            curr = curr.next
            if prev == self.rear:
                break
        return ''.join(str_list)
    
    def delete(self, target):
        """
        delete the first occurrence
        """
        if self.rear == None:
            return False
        curr = self.rear.next  # curr at first
        prev = self.rear
        while True:
            if curr.data == target:
                prev.next = curr.next
                if curr == self.rear:
                    # curr is last node, prev becomes new last
                    if prev == self.rear:
                        # list has only one node
                        self.rear = None
                    else:
                        self.rear = prev
                return True
            prev = curr
            curr = curr.next
            if prev == self.rear:
                break
        return False
    
    def addAfter(self, newItem, afterItem):
        """
        add a new item after a specified item
        """
        """
        start from front
        """
        # if self.rear == None:
        #     return False
        # curr = self.rear.next  # curr at first
        # prev = self.rear
        # while True:
        #     if curr.data == afterItem:
        #         newNode = Node(newItem, curr.next)
        #         curr.next = newNode
        #         if curr == self.rear:
        #             # newNode becomes new last
        #             self.rear = newNode
        #         return True
        #     prev = curr
        #     curr = curr.next
        #     if prev == self.rear:
        #         break
        # return False

        """
        start from rear
        """
        if self.rear == None:
            return False
        curr = self.rear
        while True:
            if curr.data == afterItem:
                newNode = Node(newItem, curr.next)
                curr.next = newNode
                if curr == self.rear:
                    # newNode becomes new last
                    self.rear = newNode
                return True
            curr = curr.next
            if curr == self.rear:
                break
        return False

class DoublyLinkedList:
    def __init__(self, front_=None):
        self.front = front_
    
    def __str__(self):
        if self.front == None:
            return 'empty list'
        str_list = [str(self.front.data)]
        curr = self.front.next
        while curr != None:
            str_list.append(' -> ')
            str_list.append(str(curr.data))
            curr = curr.next
        return ''.join(str_list)
    
    def append(self, newItem):
        prev = None
        curr = self.front
        while curr != None:
            prev = curr
            curr = curr.next
        newNode = DLLNode(newItem, None, prev)
        if prev == None:
            self.front = newNode
        else:
            prev.next = newNode
    
    def getPointer(self, targetItem):
        curr = self.front
        while curr != None:
            if curr.data == targetItem:
                return curr
            curr = curr.next
        return None
    
    def reverse(self):
        if self.front == None:
            return None
        rear = self.front
        prev = None
        while rear != None:
            # swap next and prev
            temp = rear.next
            rear.next = rear.prev
            rear.prev = temp
            prev = rear
            rear = temp
        self.front = prev
        return prev
    
    def moveToFront(self, target):
        """
        move a node (given a pointer to it) to the front of a DLL
        """
        if target == None or self.front == None or target == self.front:
            return None
        # delink the target (target.prev can't be None)
        target.prev.next = target.next
        if target.next != None:
            target.next.prev = target.prev
        target.next = self.front
        target.prev = None
        self.front.prev = target
        self.front = target
        return target


def merge(frontL1, frontL2):
    if frontL1 == None:
        return frontL2
    if frontL2 == None:
        return frontL1
    if int(frontL1.data) < int(frontL2.data):
        frontL1.next = merge(frontL1.next, frontL2)
        return frontL1
    elif int(frontL1.data) > int(frontL2.data):
        frontL2.next = merge(frontL1, frontL2.next)
        return frontL2
    else:
        frontL1.next = merge(frontL1.next, frontL2.next)
        return frontL1

def merge_nonrecursive(frontL1, frontL2):
    first = None
    last = None
    while frontL1 != None and frontL2 != None:
        if int(frontL1.data) < int(frontL2.data):
            if last == None:
                first = frontL1
            else:
                last.next = frontL1
            last = frontL1
            frontL1 = frontL1.next
        elif int(frontL1.data) > int(frontL2.data):
            if last == None:
                first = frontL2
            else:
                last.next = frontL2
            last = frontL2
            frontL2 = frontL2.next
        else:
            if last == None:
                first = frontL1
            else:
                last.next = frontL1
            last = frontL1
            frontL1 = frontL1.next
            frontL2 = frontL2.next
    if frontL1 != None:
        last.next = frontL1
    if frontL2 != None:
        last.next = frontL2
    return first

def deleteAll(front, targetItem):
        if front == None:
            return None
        if front.data == targetItem:
            return deleteAll(front.next, targetItem)
        else:
            front.next = deleteAll(front.next, targetItem)
            return front


def test0():
    # node3 = Node('c', None)
    # node2 = Node('b', node3)
    # node1 = Node('a', node2)
    # list1 = LinkedList(node1)
    # print('list1: ', end="")
    # print(list1)
    # print('len of list1: %d' % len(list1))
    # list2 = LinkedList(None)
    # print('list2: ', end="")
    # print(list2)

    list0 = CircularLinkedList(None)
    print(list0)
    print('len of list0: %d' % len(list0))

    node1 = Node('a', None)
    node1.next = node1
    list1 = CircularLinkedList(node1)
    print(list1)
    print('len of list1: %d' % len(list1))

    node2 = Node('b', None)
    node1 = Node('a', node2)
    node2.next = node1
    list2 = CircularLinkedList(node2)
    print(list2)
    print('len of list2: %d' % len(list2))

    node3 = Node('c', None)
    node2 = Node('b', node3)
    node1 = Node('a', node2)
    node3.next = node1
    list3 = CircularLinkedList(node3)
    print(list3)
    print('len of list3: %d' % len(list3))

def test1():
    node1 = Node('a', None)
    node1.next = node1
    list1 = CircularLinkedList(node1)
    print(list1)

    node2 = Node('b', None)
    node1 = Node('a', node2)
    node2.next = node1
    list2 = CircularLinkedList(node2)
    print(list2)

    node3 = Node('c', None)
    node2 = Node('b', node3)
    node1 = Node('a', node2)
    node3.next = node1
    list3 = CircularLinkedList(node3)
    print(list3)

    print('delete b from list3...')
    list3.delete('b')
    print(list3)

    print('delete b from list2...')
    list2.delete('b')
    print(list2)

    print('delete a from list1...')
    list1.delete('a')
    print(list1)

def test2():
    node1 = Node('a', None)
    node1.next = node1
    list1 = CircularLinkedList(node1)
    print(list1)

    node2 = Node('b', None)
    node1 = Node('a', node2)
    node2.next = node1
    list2 = CircularLinkedList(node2)
    print(list2)

    node3 = Node('c', None)
    node2 = Node('b', node3)
    node1 = Node('a', node2)
    node3.next = node1
    list3 = CircularLinkedList(node3)
    print(list3)

    print('add d after c in list3...')
    list3.addAfter('d', 'c')
    print(list3)

    print('add 2 after a in list3...')
    list3.addAfter('2', 'a')
    print(list3)

def test3():
    l = DoublyLinkedList()
    for i in ['a', 'b', 'c']:
        l.append(i)
    print(l)

    print('move a to the front...')
    l.moveToFront(l.getPointer('a'))
    print(l)

    print('move b to the front...')
    l.moveToFront(l.getPointer('b'))
    print(l)

    print('move c to the front...')
    l.moveToFront(l.getPointer('c'))
    print(l)

def test4():
    l = DoublyLinkedList()
    for i in ['a', 'b', 'c']:
        l.append(i)
    print(l)

    print('reverse...')
    l.reverse()
    print(l)

def test5():
    l = LinkedList()
    for i in ['a', 'b', 'b', 'c', 'b']:
        l.append(i)
    print(l)

    print('delete all b...')
    l.front = deleteAll(l.front, 'b')
    print(l)

def test6():
    l1 = LinkedList()
    for i in [3, 9, 12, 15]:
        l1.append(i)
    print(l1)

    l2 = LinkedList()
    for i in [2, 3, 6, 12]:
        l2.append(i)
    print(l2)

    l = LinkedList()
    l.front = merge_nonrecursive(l1.front, l2.front)
    print(l)

    # print(l1)
    # print(l2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('test_number', type=int, default=0)
    opt = parser.parse_args()
    eval('test%d()' % opt.test_number)
