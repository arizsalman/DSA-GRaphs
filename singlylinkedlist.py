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

# class New:
#   def __init__(self, data ):
#     self.data =data
#     self.next= None 
 
#   def insert ( self):
#     pass 
    

def rec(n):
  if n >0 :
    print (n-1)
    rec(n-1)
rec(5)

def fab (n):
   if n == 0 or n==1:
     return 1
   else:
     return fab(n-1)+fab(n-2)
     
print(fab(4))
