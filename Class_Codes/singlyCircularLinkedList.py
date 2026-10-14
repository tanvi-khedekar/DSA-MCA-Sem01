class Node:
  def _init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
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