"""Graphs is Tree """

# def func(node):
#   res =[]
#   def func2(nod):
#     if not node:

#       return node
#     func2(node.left)
#     res.append (node.val)
#     func2(node. right)
#   func2(node)
  
#   return res
# print (func [0,1,2,3])


def func(prices):
# prices=[1,2,1,3] 
    if not prices:

            return 0 
    min_price= prices[0]
    max_profit=0
    for price in prices[1:]:
        if price<min_price:
            min_price=price
        else:
            profit=price-min_price   
            max_profit= max(profit, max_profit) 
    return max_profit
print (func ([1,2,2,3,1]))

