from __future__ import print_function
import argparse
import numpy

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

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, val):
        self.queue.insert(0, val)
    
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            return self.queue.pop()
    
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return self.size() == 0
    
    def __str__(self):
        if self.isEmpty():
            return 'empty queue'
        return str(self.queue[::-1]).strip('[]')
    
    # for problem 6
    def evenSplit(self):
        q = Queue()
        for pos in range(1, self.size()+1):
            if pos % 2 == 1:
                self.enqueue(self.dequeue())
            else:
                q.enqueue(self.dequeue())
        return q

# problem 1
def size(S):
    temp = Stack()
    count = 0
    while not S.isEmpty():
        temp.push(S.pop())
        count += 1
    while not temp.isEmpty():
        S.push(temp.pop())
    return count

# problem 2
def postfixEvaluate(expr):
    operand = Stack()
    for ch in expr.split():
        if ch in ['+', '-', '*', '/']:
            second = operand.pop()
            first = operand.pop()
            if ch == '+':
                operand.push(first + second)
            elif ch == '-':
                operand.push(first - second)
            elif ch == '*':
                operand.push(first * second)
            elif ch == '/':
                operand.push(first / second)
        else:
            operand.push(float(ch))
    return operand.pop()

# problem 3
class P3Array:
    def __init__(self):
        self.array = numpy.zeros(100)
        self.length = 0
    
    def __len__(self):
        return self.length
    
    def capacity(self):
        return len(self.array)
    
    def append(self, elem):
        global COUNTER
        if self.length >= self.capacity():
            new_array = numpy.zeros(self.capacity()+50)
            COUNTER += 1  # allocation
            for i in range(self.length):
                new_array[i] = self.array[i]
                COUNTER += 1  # write/copy
            self.array = new_array
        self.array[self.length] = elem
        COUNTER += 1  # write/copy
        self.length += 1
    
    def __str__(self):
        return str(self.array[:self.length])

# problem 4
class P4Array:
    def __init__(self):
        self.array = numpy.zeros(5)
        self.length = 0
    
    def __len__(self):
        return self.length
    
    def capacity(self):
        return len(self.array)
    
    def append(self, elem):
        global COUNTER
        if self.length >= self.capacity():
            new_array = numpy.zeros(self.capacity()*2)
            COUNTER += 1  # allocation
            for i in range(self.length):
                new_array[i] = self.array[i]
                COUNTER += 1  # write/copy
            self.array = new_array
        self.array[self.length] = elem
        COUNTER += 1  # write/copy
        self.length += 1
    
    def __str__(self):
        return str(self.array[:self.length])

# for problem 5
def peek(q):
    if q.isEmpty():
        return None
    res = q.dequeue()
    q.enqueue(res)

    for _ in range(q.size()-1):
        q.enqueue(q.dequeue())
    
    return res


## tests
def test1():
    S = Stack()
    for i in [1, 2, 3]:
        S.push(i)
    print(S)
    print('size of S: %d' % size(S))
    print(S)

def test2():
    expr = '2'
    print('%s = %f' % (expr, postfixEvaluate(expr)))

    expr = '2 3 +'
    print('%s = %f' % (expr, postfixEvaluate(expr)))

    expr = '2 3 4 + *'
    print('%s = %f' % (expr, postfixEvaluate(expr)))

    expr = '2 3 4 - * 5 /'
    print('%s = %f' % (expr, postfixEvaluate(expr)))

def test3():
    global COUNTER
    a = P3Array()
    COUNTER = 0
    for i in range(1000):
        a.append(i)
    print('# of unit of work: %d' % COUNTER)
    # print(a)

def test4():
    global COUNTER
    a = P4Array()
    COUNTER = 0
    for i in range(100):
        a.append(i)
    print('# of unit of work: %d' % COUNTER)
    # print(a)

def test5():
    q = Queue()
    for i in [1, 2, 3]:
        q.enqueue(i)
    print(q)
    print('front: %d' % peek(q))
    print(q)

def test6():
    q1 = Queue()
    for i in [1, 2, 3, 4, 5, 6]:
        q1.enqueue(i)
    print(q1)
    print(q1.evenSplit())
    print(q1)

    q1 = Queue()
    for i in [1, 2, 3, 4, 5]:
        q1.enqueue(i)
    print(q1)
    print(q1.evenSplit())
    print(q1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('test_number', type=int, default=0)
    opt = parser.parse_args()
    eval('test%d()' % opt.test_number)
