# 07-10-2026

# 1. Creating LinkedList
# 2. Printing LinkdedList
# 3. Counting LinkedList
# 4. Inserting at Beginning
# 5. Inserting at End
# 6. Inserting at Specific Position

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None
        
    def insertAtBegin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAtEnd(self,data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = new_node
    
    def printList(self):
        if(self.head == None):
            print("List is Empty!")
        else:
            temp = self.head
            while(temp):
                print(temp.data,end=" -> ")
                temp = temp.next
            print("None")
    
    def insertAtPos(self,data,pos):
        new_node = Node(data)
        if pos<1 or pos>self.countList()+1:
            print("Inavlid Postion")
        elif(pos==1):
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for i in range(pos-2):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            
    def countList(self):
        count = 0
        if(self.head == None):
            print("List is Empty!")
        else:
            temp = self.head
            while(temp):
                count = count+1
                temp = temp.next
            return count
        

ob1 = SinglyLL()
ob1.insertAtEnd(8)
ob1.printList()
ob1.insertAtBegin(1)
ob1.printList()

for x in [10,20,30,40]:
    ob1.insertAtEnd(x)
ob1.printList()

print(ob1.countList())

ob1.insertAtPos(33,0)
ob1.insertAtPos(34,8)
ob1.printList()

ob1.insertAtEnd(50)
ob1.printList()
print(ob1.countList())
ob1.insertAtPos(60,8)
ob1.printList()
ob1.insertAtPos(63,10)