# Q2. Write a program to perform the following operations on a Linear Queue
# 1. Enqueue  2. Dequeue  3. Display  4. Reverse the queue using stack
# 5. Merge two queues into one  6. Check if two queues are identical
# Queue implementation using Linked List

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


# Stack (needed for reversing the queue)
class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            return None
        temp = self.top
        value = temp.data
        self.top = self.top.next
        temp = None
        return value


class LQueue:
    def __init__(self):
        self.front = self.rear = None

    def isempty(self):
        return self.front is None

    # 1. Enqueue
    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    # 2. Dequeue
    def dequeue(self):
        if self.isempty():
            print("Queue is Empty")
            return None
        temp = self.front
        value = temp.data
        self.front = self.front.next
        if self.front is None:           # only one node was present
            self.rear = None
        temp = None
        return value

    # 3. Display
    def display(self):
        if self.isempty():
            print("Queue is Empty")
        else:
            temp = self.front
            while temp:
                print(temp.data, end="->")
                temp = temp.next
            print("None")

    # 4. Reverse the queue using stack
    def reverse(self):
        s = Stack()
        while not self.isempty():        # queue -> stack
            s.push(Node(self.dequeue()))
        while not s.isempty():           # stack -> queue (reversed)
            self.enqueue(Node(s.pop()))

    # 5. Merge two queues into one (self first, then other)
    def merge(self, other):
        merged = LQueue()
        temp = self.front
        while temp:
            merged.enqueue(Node(temp.data))
            temp = temp.next
        temp = other.front
        while temp:
            merged.enqueue(Node(temp.data))
            temp = temp.next
        return merged

    # 6. Check if two queues are identical
    def is_identical(self, other):
        t1 = self.front
        t2 = other.front
        while t1 and t2:
            if t1.data != t2.data:
                return False
            t1 = t1.next
            t2 = t2.next
        return t1 is None and t2 is None


# ---------------- Main Program ----------------
que = LQueue()

print("--- Enqueue Operation ---")
for v in [10, 20, 30, 40, 50]:
    que.enqueue(Node(v))
    print("Enqueued Element :", v)

print("\n--- Display Operation ---")
que.display()

print("\n--- Dequeue Operation ---")
print("Deleted node :", que.dequeue())

print("\n--- Display After Dequeue ---")
que.display()

print("\n--- Reverse the Queue using Stack ---")
print("Original Queue :", end=" ")
que.display()
que.reverse()
print("Reversed Queue :", end=" ")
que.display()

print("\n--- Merge Two Queues ---")
q1 = LQueue()
q2 = LQueue()
for v in [1, 2, 3]:
    q1.enqueue(Node(v))
for v in [4, 5, 6]:
    q2.enqueue(Node(v))
print("Queue 1 :", end=" ")
q1.display()
print("Queue 2 :", end=" ")
q2.display()
merged = q1.merge(q2)
print("Merged Queue :", end=" ")
merged.display()

print("\n--- Check if Two Queues are Identical ---")
qa = LQueue()
qb = LQueue()
qc = LQueue()
for v in [1, 2, 3]:
    qa.enqueue(Node(v))
    qb.enqueue(Node(v))
for v in [1, 2, 4]:
    qc.enqueue(Node(v))
print("Queue A :", end=" ")
qa.display()
print("Queue B :", end=" ")
qb.display()
print("Queue C :", end=" ")
qc.display()

if qa.is_identical(qb):
    print("Queue A and Queue B are identical")
else:
    print("Queue A and Queue B are NOT identical")

if qa.is_identical(qc):
    print("Queue A and Queue C are identical")
else:
    print("Queue A and Queue C are NOT identical")