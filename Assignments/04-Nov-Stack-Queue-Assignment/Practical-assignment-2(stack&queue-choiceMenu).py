# IT12 Data Structure and Algorithms - Practical Assignment 1
# Q1: Stack using Linked List
# Q2: Linear Queue using Linked List


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


# Reads an integer safely (asks again on empty / invalid input)
def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


# ---------------------------------------------------------------
# Q1. STACK
# ---------------------------------------------------------------
class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    # 1. Push
    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    # 2. Pop (returns the popped value, None if empty)
    def pop(self):
        if self.isempty():
            print("Stack is Empty")
            return None
        temp = self.top
        value = temp.data
        self.top = self.top.next
        temp = None
        return value

    # 3. Display
    def display(self):
        if self.isempty():
            print("Stack is Empty")
        else:
            print("Stack Contains (top to bottom)...")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

    # 4. Reverse string using stack
    def reverse_string(self, text):
        for ch in text:                 # push every character
            self.push(Node(ch))
        result = ""
        while not self.isempty():       # pop all -> reverse order
            result = result + self.pop()
        return result

    # 5. Reverse stack using another stack
    def reverse_stack(self):
        other = Stack()
        while not self.isempty():
            other.push(Node(self.pop()))
        return other                    # holds elements in reverse order


def stack_menu():
    st = Stack()
    while True:
        print("\n--- STACK MENU ---")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Reverse String using Stack")
        print("5. Reverse Stack using another Stack")
        print("6. Exit")
        ch = read_int("Enter your choice: ")

        if ch == 1:
            val = read_int("Enter value to push: ")
            st.push(Node(val))
        elif ch == 2:
            val = st.pop()
            if val is not None:
                print("Popped Element :", val)
        elif ch == 3:
            st.display()
        elif ch == 4:
            s = input("Enter a string: ")
            temp_stack = Stack()
            print("Reversed String :", temp_stack.reverse_string(s))
        elif ch == 5:
            if st.isempty():
                print("Stack is Empty")
            else:
                print("Original Stack:")
                st.display()
                st = st.reverse_stack()
                print("Reversed Stack:")
                st.display()
        elif ch == 6:
            break
        else:
            print("Invalid choice")


# ---------------------------------------------------------------
# Q2. LINEAR QUEUE
# ---------------------------------------------------------------
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

    # 2. Dequeue (returns the deleted value, None if empty)
    def dequeue(self):
        if self.isempty():
            print("Queue is Empty")
            return None
        temp = self.front
        value = temp.data
        self.front = self.front.next
        if self.front is None:          # only one node was present
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
        while not self.isempty():       # queue -> stack
            s.push(Node(self.dequeue()))
        while not s.isempty():          # stack -> queue (reversed)
            self.enqueue(Node(s.pop()))

    # 5. Merge two queues (new queue: self first, then other)
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


def read_queue(name):
    q = LQueue()
    n = read_int("How many elements in " + name + "? ")
    for i in range(n):
        q.enqueue(Node(read_int("Enter element: ")))
    return q


def queue_menu():
    que = LQueue()
    while True:
        print("\n--- LINEAR QUEUE MENU ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Reverse the queue using stack")
        print("5. Merge two queues into one")
        print("6. Check if two queues are identical")
        print("7. Exit")
        ch = read_int("Enter your choice: ")

        if ch == 1:
            val = read_int("Enter value to enqueue: ")
            que.enqueue(Node(val))
        elif ch == 2:
            val = que.dequeue()
            if val is not None:
                print("Deleted node:", val)
        elif ch == 3:
            que.display()
        elif ch == 4:
            que.reverse()
            print("Queue after reversing:")
            que.display()
        elif ch == 5:
            q1 = read_queue("Queue 1")
            q2 = read_queue("Queue 2")
            print("Queue 1:", end=" ")
            q1.display()
            print("Queue 2:", end=" ")
            q2.display()
            m = q1.merge(q2)
            print("Merged Queue:", end=" ")
            m.display()
        elif ch == 6:
            q1 = read_queue("Queue 1")
            q2 = read_queue("Queue 2")
            if q1.is_identical(q2):
                print("The queues are identical")
            else:
                print("The queues are NOT identical")
        elif ch == 7:
            break
        else:
            print("Invalid choice")


# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
while True:
    print("\n===== MAIN MENU =====")
    print("1. Stack (Q1)")
    print("2. Linear Queue (Q2)")
    print("3. Exit")
    c = read_int("Enter your choice: ")
    if c == 1:
        stack_menu()
    elif c == 2:
        queue_menu()
    elif c == 3:
        break
    else:
        print("Invalid choice")