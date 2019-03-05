from __future__ import print_function
import argparse

COUNTER = 0

class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.stack.pop()

    def push(self,val):
        return self.stack.append(val)

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return self.size() == 0
    
    def __str__(self):
        if self.isEmpty():
            return 'empty stack'
        return str(self.stack).strip('[]')

class BSTNode:
    def __init__(self, data=''):
        self.data = data
        self.left = None
        self.right = None
        self.rightSize = 0

class BST:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.root == None:
            return 'empty BST'
        str_list = [str(i) for i in inorder(self.root)]
        return '(inorder) ' + ' '.join(str_list)
    
    def __repr__(self):
        return 'BST: ' + self.__str__()
    
    def toStringRightSize(self):
        if self.root == None:
            return 'empty BST'
        str_list = ['(%d,%d)'%(i, s) for i, s in inorder_rightSize(self.root)]
        return '(inorder) ' + ' '.join(str_list)
    
    def insert(self, target):
        prev = None
        curr = self.root
        while curr != None:
            c = target - curr.data
            if c == 0:
                raise ValueError('Duplicate key')
            prev = curr
            curr = curr.left if c < 0 else curr.right
            if c > 0:
                prev.rightSize += 1
        newNode = BSTNode(target)
        self.size += 1
        if self.root == None:
            self.root = newNode
            return
        if c < 0:
            prev.left = newNode
        else:
            prev.right = newNode
    
    def insert_recursive(self, target, root=None):
        # P3
        if root == None:
            self.size += 1
            return BSTNode(target)
        c = target - root.data
        if c == 0:
            raise ValueError('Duplicate key')
        if c < 0:
            root.left = self.insert_recursive(target, root.left)
        else:
            root.right = self.insert_recursive(target, root.right)
            root.rightSize += 1
        return root
    
    def delete(self, target):
        # P2
        global COUNTER

        # locate target
        prev = None
        curr = self.root
        COUNTER += 2
        while curr != None:
            COUNTER += 1  # equal comparison
            if curr.data == target:
                break
            c = target - curr.data
            COUNTER += 1
            prev = curr
            curr = curr.left if c < 0 else curr.right
            COUNTER += 2
        if curr == None:
            raise ValueError('Target not found')
        self.size -= 1
        
        # check number of child
        if curr.left == None:
            if c < 0:
                prev.left = curr.right
                COUNTER += 1
            else:
                prev.right = curr.right
                COUNTER += 1
            return
        if curr.right == None:
            if c < 0:
                prev.left = curr.left
                COUNTER += 1
            else:
                prev.right = curr.left
                COUNTER += 1
            return

        # locate smallest value in right subtree, successor
        temp = curr
        COUNTER += 1
        prev = curr
        curr = curr.right
        COUNTER += 2
        while curr.left != None:
            prev = curr
            curr = curr.left
            COUNTER += 2
        
        # overwite target with successor
        temp.data = curr.data

        # delete successor
        if curr.right == None:
            prev.left = None
            COUNTER += 1
        else:
            prev.left = curr.right
            COUNTER += 1
    
    def kthLargest(self, k=1):
        # P6
        prev = None
        curr = self.root
        numLarger = curr.rightSize
        while True:
            if numLarger == k-1:
                break
            prev = curr
            if numLarger > k-1:
                # search in right subtree
                curr = curr.right
                numLarger -= prev.rightSize - curr.rightSize
            else:
                # search in left subtree
                curr = curr.left
                numLarger += 1 + curr.rightSize
        return curr.data

# helper function, inorder traversal
def inorder(root):
    if root == None:
        return
    # left subtree
    for i in inorder(root.left):
        yield i
    # root node
    yield root.data
    # right subtree
    for i in inorder(root.right):
        yield i

def inorder_rightSize(root):
    if root == None:
        return
    # left subtree
    for i, s in inorder_rightSize(root.left):
        yield i, s
    # root node
    yield root.data, root.rightSize
    # right subtree
    for i, s in inorder_rightSize(root.right):
        yield i, s

# non-recursive inorder traversal
def inorder_stack(root):
    S = Stack()
    curr = root
    while curr != None or not S.isEmpty():
        # find left most
        while curr != None:
            S.push(curr)
            curr = curr.left

        # pop
        curr = S.pop()
        yield curr.data

        # right tree
        curr = curr.right

# P4
def keysInRange(root, minVal, maxVal):
    global COUNTER
    
    if root == None:
        return
    c1 = minVal - root.data
    c2 = root.data - maxVal
    COUNTER += 2
    if c1 <= 0 and c2 <= 0:
        # min <= root <= max
        yield root.data
    if c1 < 0:
        # min < root
        for i in keysInRange(root.left, minVal, maxVal):
            yield i
    if c2 < 0:
        # root < max
        for i in keysInRange(root.right, minVal, maxVal):
            yield i

# P5
def reverseKeys(root):
    if root == None:
        return
    reverseKeys(root.left)
    reverseKeys(root.right)
    root.left, root.right = root.right, root.left

# P6
def kthLargest(root, k=1):
    if root.rightSize == k-1:
        return root.data
    if root.rightSize > k-1:
        return kthLargest(root.right, k)
    else:
        return kthLargest(root.left, k-1-root.rightSize)

def test0():
    t = BST()
    for i in [10, 17, 3, 90, 22, 7, 40, 15]:
        t.insert(i)
    print(t)

    t = BST()
    for i in [25, 10, 40, 2, 20, 30, 45, 15, 35]:
        t.insert(i)
    print(t)

def test2():
    global COUNTER
    t = BST()
    for i in [10, 17, 3, 90, 22, 7, 40, 15]:
        t.insert(i)
    print(t)
    COUNTER = 0
    t.delete(17)
    print(t)
    print('# of unit of work: %d' % COUNTER)

def test3():
    t1 = BST()
    for i in [10, 17, 3, 90, 22, 7, 40, 15]:
        t1.insert(i)
    print('length: %d' % len(t1))
    print(t1)
    
    t2 = BST()
    for i in [10, 17, 3, 90, 22, 7, 40, 15]:
        t2.root = t2.insert_recursive(i, t2.root)
    print('length: %d' % len(t2))
    print(t2)

def test4():
    global COUNTER
    t = BST()
    for i in [10, 17, 3, 90, 22, 7, 40, 15]:
        t.insert(i)
    print(t)
    print('keys in range [4, 20]: ')
    COUNTER = 0
    for i in keysInRange(t.root, 4, 20):
        print(i)
    print('# of unit of work: %d' % COUNTER)

def test5():
    t = BST()
    for i in [10, 17, 3, 90, 22, 7, 40, 15]:
        t.insert(i)
    print(t)
    print('reverse keys: ')
    reverseKeys(t.root)
    print(t)

def test6():
    t = BST()
    for i in [10, 17, 3, 90, 22, 7, 40, 15]:
        t.insert(i)
    print(t)
    for k in range(1, len(t)+1):
        i = kthLargest(t.root, k)
        print('%d-th largest: %d'%(k, i))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('test_number', type=int, default=0)
    opt = parser.parse_args()
    eval('test%d()' % opt.test_number)
