# class Node:
#     def __init__(self,val):
#         self.left = None
#         self.right = None
#         self.val = val
        
    

# class Solution:
#     def find132pattern(self, nums):
#         if len(nums) < 3:
#             return False
#         l = len(nums) 
#         left = [0] * l
     
#         left_min = nums[0] 
#         for i in range(1,l-1):
#             left_min = min(nums[i],left_min) 
#             left[i] = left_min
            
#         head = Node(nums[-1])
        
#         for i in range(l-2,0,-1):
#             LE_smaller_than_current = self.insert(head,Node(nums[i]))
#             if LE_smaller_than_current > left[i]:
#                 return True
            
#         return False
            
#     def insert(self,head,node):
#         curr = head
#         largest_smallest = float('-inf') 
#         while curr:
#             if node.val > curr.val:
#                 largest_smallest = max(largest_smallest,curr.val)
#                 if curr.right:
#                     curr = curr.right
#                 else:
#                     curr.right = node
#                     curr = None
#             else:
#                 if curr.left:
#                     curr = curr.left
#                 else:
#                     curr.left = node
#                     curr = None
        
#         return largest_smallest        

class Solution:
    def find132pattern(self,nums):
        if len(nums) < 3:
            return False
        s3_candidate = float('inf')
        stack = []
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < s3_candidate:
                return True
            while len(stack) > 0 and stack[-1] > nums[i]:
                s3_candidate = stack.pop()
            stack.append(nums[i])
        return False


s = Solution()
print(s.find132pattern([-2,1,2,-2,1,2]))
            