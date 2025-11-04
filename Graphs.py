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


# def func(prices):
# # prices=[1,2,1,3] 
#     if not prices:

#             return 0 
#     min_price= prices[0]
#     max_profit=0
#     for price in prices[1:]:
#         if price<min_price:
#             min_price=price
#         else:
#             profit=price-min_price   
#             max_profit= max(profit, max_profit) 
#     return max_profit
# print (func ([1,2,2,3,1]))



# """Leet Code no 53 s"""

# def fun(nums):
#      n=len(nums)
#      maxi=float("-inf")
#      total=0
#      for i in range(n):
#           total =total +nums[i]
#           maxi=max(maxi, total )
#           if total < 0:
#                total =0
#      return maxi 
# print (fun( [-2,1,-3,4,-1,2,1,-5,4]))


# leet code  no 256 

def func (nums):
     n=len(nums)    
     dic={}
     for i in range (0, n+1):
          dic[i]=0
     for num in nums :
          dic[num]=1
     for k, v in dic.items():
          if v ==0 :
               return k 
    #  return dic 
print( func ([3,0,1]))

def func(nums):
    n = len(nums)
    dic = {}
    for i in range(0, n + 1):
        dic[i] = 0
    for num in nums:
        dic[num] = 1
    for k, v in dic.items():
        if v == 0:
            return k

print(func([3, 0, 1]))