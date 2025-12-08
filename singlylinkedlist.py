class Node:
  def __init__(self, data ):
    self.data= data 
    self.next=None

head = Node (1)
head.next=Node(2)
head.next.next=Node(3)

current_node = head 
while current_node is not None :
  print ( current_node.data , end="-> ")
  current_node =current_node.next

print( "None ")