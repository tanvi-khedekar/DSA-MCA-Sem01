class Node:
  def _init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def append(self, new_node):
    new_node.next=self.head

  def insert(self, new_node, pos):
    if pos == 1:  #insert node at first position
      temp=self.head
      while(temp.next != self.head):  #find last node
        temp=temp.next
      new_node.next=self.head
      self.head=new_node
      temp.next=self.head
    else: #insert nodefrom 2nd to last position
      p=1
      temp=self.head
      while(p!=pos-1):
        temp=temp.next
        p+=1

  def delete(self, value):
    temp=self.head
    prev=None
    if temp.data==value:    #first node to delete
      while(temp.next != self.head):
        temp.next=self.head
      self.head=self.head.next
      temp.next=self.head
    else:
      while(temp.data != value and temp):
        prev=temp
        temp=temp.next
        if temp == self.head:
          print("Value is not present in the list")
          return
      prev.next=temp.next
      temp=None

  def print(self):
    print()


list=LinkedList()
n1=Node(10)
n2=Node(20)
list