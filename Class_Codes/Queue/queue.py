#linear queue using linked list

class node:
    def __init__(self,value):
        self.data=value
        self.next=None
       
class LQueue:  
    def __init__(self):      
         self.front=self.rear=None
    def enqueue(self, new_node) :
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node  
            
    def dequeue(self):
        temp=self.front
        print("deleted node:",temp.data)
        self.front=self.front.next
        if self.front==None: #if there is only one node
            print("Queue is empty")
            self.rear=None
        temp=None    
               
    def print(self):
        temp=self.front
        while temp:
            print(temp.data, end="->")             
            temp=temp.next       
que=LQueue()  
          
que.enqueue(node(10))
que.enqueue(node(20))
que.enqueue(node(30))
que.enqueue(node(40))
que.enqueue(node(50))

que.print()

que.dequeue()
que.print()

# output: 
# 10->20->30->40->50->deleted node: 10
# 20->30->40->50->