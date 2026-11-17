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

    # Helper to display priority status text
    def get_status(self, pr):
        if pr == 1:
            return "Critical"
        elif pr == 2:
            return "Serious"
        elif pr == 3:
            return "Normal"
        return "Unknown"

    # 1. Add Patient (enqueue)
    def enqueue(self, id, name, pr):
        node = Node(id, name, pr)

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
        print("Treated and removed patient:", self.front.id, self.front.name)
        temp = self.front
        self.front = self.front.next
        temp.next = None

    # 4. Display all waiting patients in priority order (display_all)
    def display_all(self):
        if self.front == None:
            print("No waiting patients")
            return
        temp = self.front
        print("\nWaiting Patients (Priority Order):")
        while temp:
            print(temp.id, temp.name, f"- Priority {temp.pr} ({self.get_status(temp.pr)})")
            temp = temp.next
        print()


# Menu-driven execution to accept user input
q = PriorityQueue()

while True:
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Treated Patient")
    print("4. Display All Waiting Patients")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        pid = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        pr = int(input("Enter Priority (1: Critical, 2: Serious, 3: Normal): "))
        q.enqueue(pid, name, pr)
    elif choice == 2:
        q.display_next()
    elif choice == 3:
        q.dequeue()
    elif choice == 4:
        q.display_all()
    elif choice == 5:
        break
    else:
        print("Invalid choice")