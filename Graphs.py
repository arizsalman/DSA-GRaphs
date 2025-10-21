"""Graphs is Tree """

def func(node):
  res =[]
  def func2(nod):
    if not node:

      return node
    func2(node.left)
    res.append (node.val)
    func2(node. right)
  func2(node)
  
  return res
print (func [0,1,2,3])