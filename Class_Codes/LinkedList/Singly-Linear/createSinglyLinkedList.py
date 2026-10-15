#creation of singly linked list

class Node:
    def __init__(self, val):
        self.data=val 
        self.next=None
        
class LinkedList:
    def __init__(self):
            self.head=None
            
    def append(self, new_node):
        if (self.head==None): #linklist in constructor
             self.head=new_node
        else:
             temp=self.head
             while(temp.next != None ):
                  temp=temp.next
             temp.next=new_node #appending new node
             
    def print(self):
         temp=self.head
         while temp:
              print(temp.data,end="->")
              temp=temp.next
         print("None")

list=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.print()