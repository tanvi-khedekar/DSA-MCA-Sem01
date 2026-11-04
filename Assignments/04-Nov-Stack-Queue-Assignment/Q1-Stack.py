# Q1. Create a Stack with the following operations
# 1. Push  2. Pop  3. Display  4. Reverse String using Stack
# 5. Reverse Stack using another Stack
# Stack implementation using Linked List

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    # 1. Push
    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    # 2. Pop
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
        s = Stack()
        for ch in text:                   # push every character
            s.push(Node(ch))
        result = ""
        while not s.isempty():            # pop every character
            result = result + s.pop()
        return result

    # 5. Reverse stack using another stack
    def reverse_stack(self):
        other = Stack()
        while not self.isempty():
            other.push(Node(self.pop()))
        return other


# ---------------- Main Program ----------------
st = Stack()

print("--- Push Operation ---")
for v in [10, 20, 30, 40, 50]:
    st.push(Node(v))
    print("Pushed Element :", v)

print("\n--- Display Operation ---")
st.display()

print("\n--- Pop Operation ---")
print("Popped Element :", st.pop())

print("\n--- Display After Pop ---")
st.display()

print("\n--- Reverse String using Stack ---")
text = "HELLO"
print("Original String :", text)
print("Reversed String :", st.reverse_string(text))

print("\n--- Reverse Stack using another Stack ---")
print("Original Stack:")
st.display()
st1 = st.reverse_stack()
print("Reversed Stack:")
st1.display()