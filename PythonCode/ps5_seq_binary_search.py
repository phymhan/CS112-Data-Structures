from __future__ import print_function
import argparse

class Node:
    def __init__(self, data_='', next_=None):
        self.data = data_
        self.next = next_

class LinkedList:
    def __init__(self, front_=None):
        if isinstance(front_, list):
            self.fromList(front_)
        else:
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
    
    def fromList(self, l):
        rear = None
        for i in l:
            newNode = Node(i, None)
            if rear == None:
                # first node
                self.front = newNode
                rear = newNode
            else:
                rear.next = newNode
                rear = newNode
    
    def moveTowardFront(self, targetItem):
        """
        Code for P2
        """
        curr = self.front
        prev = None
        while curr != None:
            if curr.data == targetItem:
                break
            else:
                prev = curr
                curr = curr.next
        if curr == None:
            # not found
            return False
        if prev == None:
            # front node, do nothing
            return True
        # Switch with prev
        # only swap data
        prev.data, curr.data = curr.data, prev.data
        return True


def test2():
    l = LinkedList([1, 2, 3, 4, 5])
    print(l)
    print('search for 3...')
    if l.moveTowardFront(3):
        print('target found')
        print(l)
    else:
        print('not found')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('test_number', type=int, default=0)
    opt = parser.parse_args()
    eval('test%d()' % opt.test_number)
