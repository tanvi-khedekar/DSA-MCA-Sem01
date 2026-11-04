
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

    # 1. create singly linked list-append(creates nodes with positive and negative numbers)
    def create_list(self, values):
      for value in values:
        self.insert_at_end(value)


    def insert_at_end(self, data):
      new_node = Node(data)

      if self.head is None:
        self.head = new_node
      else:
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
          
    # 2. Traverse and print the node values

    def display(self):
      current_node = self.head

      while current_node is not None:
           print(current_node.data, end=" -> ")
           current_node = current_node.next

      print()

    # 3. Insert node at a specific position

    def insert_at_position(self, data, position):
            new_node = Node(data)
    
            if position == 0:
                new_node.next = self.head
                self.head = new_node
                return
    
            current_node = self.head
    
            for _ in range(position - 1):
                if current_node is None:
                    print("Invalid position")
                    return
                current_node = current_node.next
    
            if current_node is None:
                print("Invalid position")
                return
    
            new_node.next = current_node.next
            current_node.next = new_node

    #def insert_at_position(self, data, position):
       

    # 4. Delete the nodes having negative values  

  # Main program
linked_list = LinkedList()

linked_list.create_list([10, 20, 30, 40])

print("Original list:")
linked_list.display()

#print("After inserting 25 at position 2:")
#linked_list.insert_at_position(25, 2)
#linked_list.display()