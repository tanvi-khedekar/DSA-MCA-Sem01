# Hospital Emergency Management
class Node:
    def __init__(self, id, name, pr):
        self.id = id
        self.name = name
        self.pr = pr
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = None

    def get_status(self, pr):
        if pr == 1:
            return "Critical"
        elif pr == 2:
            return "Serious"
        elif pr == 3:
            return "Normal"
        return "Unknown"

    # 1. Add Patient (enqueue)
    def enqueue(self, node):
        if self.front == None or node.pr < self.front.pr:
            node.next = self.front
            self.front = node
            return

        temp = self.front
        while temp.next and temp.next.pr <= node.pr:
            temp = temp.next

        node.next = temp.next
        temp.next = node

    # 2. Display the next patient to be treated (display_next)
    def display_next(self):
        if self.front == None:
            print("No patients in queue")
            return
        print("Next patient to be treated:", self.front.id, self.front.name, f"({self.get_status(self.front.pr)})")

    # 3. Remove a patient from the queue after treatment (dequeue)
    def dequeue(self):
        if self.front == None:
            print("Queue is empty")
            return
        print("Deleted patient:", self.front.id, self.front.name)
        temp = self.front
        self.front = self.front.next
        temp.next = None

    # 4. Display all waiting patients in priority order (display_all)
    def display_all(self):
        if self.front == None:
            print("No waiting patients")
            return
        temp = self.front
        print("Waiting Patients:")
        while temp:
            print(temp.id, temp.name, temp.pr, f"({self.get_status(temp.pr)})")
            temp = temp.next

q = PriorityQueue()
q.enqueue(Node(101, "Scout", 1))
q.enqueue(Node(102, "Manish", 3))
q.enqueue(Node(103, "Maya", 3))
q.enqueue(Node(104, "Kanika", 2))

q.display_all()
q.display_next()
q.dequeue()
q.display_all()