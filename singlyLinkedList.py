#Single Linear Linked List

class Node:                         #creating node
  def __init__(self, val):      #constructor that has access to first nodes' address
    self.data=val
    self.next=None

class LinkedList:
  def __init__(self):   #linkedList initialization with head being null i.e None
    self.head=None
  def append(self, new_node):
    if (self.head==None):
      self.head=new_node
    else:
      temp=self.head            #assigning head nodes value to temp
      while(temp.next):       #means temp != None(null)
        temp=temp.next
      temp.next=new_node        #appending new node

  def print(self):
    count=0
    sum=0
    temp=self.head
    while temp:
      count+=1
      if temp.data>0:       #sum of ONLY positive value nodes in the list
       sum+=temp.data       #sum of ALL values in the list
      print(temp.data)      #printing data in the list
      temp=temp.next        #in order to print alternate values, make this temp.next.next and remove above if condition
    print(count)            #printing number of values in the list
    print(sum)              #sum of all values in the list

    #in print func for printing ALTERNATE VALUES(for ODD number of nodes)
    #temp=self.head
    #while temp.next:
      #print(temp.data)
    #temp=temp.next.nex
    #if temp:
      #print(temp.data)

#creating object of class Node
list=LinkedList()
n1=Node(10)
n2=Node(-20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(-40))         #created object in the append itself for n4 apparently
list.append(Node(55))
list.print()