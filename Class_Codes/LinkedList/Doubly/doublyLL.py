# # Doubly Linked List Program--
# 1. Append the list
# 2. Insert at Position
# 3. Print list
# 4. Print list in reverse order
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None
    
    def append(self,data):      # Append node to the List
        new_node = Node(data)
        if self.head == None:       # if there are no nodes in list
            self.head = new_node
        else:                       # if there are multiple nodes
            temp = self.head
            while(temp.next!=None):
                temp = temp.next    
            temp.next = new_node
            new_node.prev = temp
    
    def printDLL(self):
        if self.head == None:
            print("DLL is Empty!")
        else:
            temp = self.head
            while(temp):
                print(temp.data,end=" <--> ")
                temp = temp.next
            print("None")
    
    def printDLLRev(self):
        if self.head == None:
            print("DLL is Empty!")
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            while(temp!=None):
                print(temp.data,end=" <--> ")
                temp = temp.prev
            print("None")
    
    def countDLL(self):
        count = 0
        if self.head == None:
            print("DLL is Empty!")
        else:
            temp = self.head
            while(temp):
                count = count+1
                temp = temp.next
        return count
    
    def insertAtPos(self,data,pos):
        new_node = Node(data)
        if pos<1 or pos>self.countDLL()+1:
            print("Invalid Position!")
        elif (pos == 1):
            if self.head == None:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        else:
            temp = self.head
            for i in range(pos-2):
                temp = temp.next
            new_node.next = temp.next
            new_node.prev = temp
            if temp.next!=None:
                temp.next.prev = new_node
            temp.next = new_node

ob1 = DoublyLL()
ob1.append(10)
ob1.printDLL()

for x in [20,30,40]:
    ob1.append(x)
ob1.printDLL()

ob1.insertAtPos(5,1)
ob1.printDLL()

ob1.insertAtPos(8,4)
ob1.printDLL()

ob1.insertAtPos(100,8)
ob1.insertAtPos(100,7)
ob1.printDLL()

ob1.printDLLRev()