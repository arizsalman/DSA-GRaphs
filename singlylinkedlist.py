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
    

# def rec(n):
#   if n >0 :
#     print (n-1)
#     rec(n-1)
# rec(5)

# def fab (n):
#    if n == 0 or n==1:
#      return 1
#    else:
#      return fab(n-1)+fab(n-2)
     
# print(fab(4))

arri=[1,2,3,4,5,6]
target=5

def nums(arri , target,left,right ):
  if left > right:
    return -1
  mid =left+(right-left)//2
  if arri[mid]==target:
    return mid
  elif arri[mid]>target:
    return nums(arri, target,left ,mid-1)

  else :
    return nums(arri, target, mid+1, right )
result =nums(arri, target, 0,len(arri)-1)
print( result )
arri = [1, 2, 3, 4, 5, 6]
target = 5

def nums(arri, target, left, right):
    if left > right:
        return -1
    mid = left + (right - left) // 2  # Corrected here
    if arri[mid] == target:
        return mid
    elif arri[mid] > target:
        return nums(arri, target, left, mid - 1)
    else:
        return nums(arri, target, mid + 1, right)

result = nums(arri, target, 0, len(arri) - 1)
print(result)  # Output: 4 (index of 5 in the list)
