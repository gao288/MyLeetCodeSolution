# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.preorder_idx = 0 
    def buildTree(self, preorder, inorder):
        index_map = {val:index for index,val in enumerate(inorder)}
        return self.dfs(preorder,inorder,index_map,0)
    def dfs(self,preorder,inorder,index_map,offset):
        if len(inorder) ==0 :
            return None
        root = TreeNode(preorder[self.preorder_idx])
        inorder_idx = index_map[preorder[self.preorder_idx]]-offset
        self.preorder_idx += 1
        root.left = self.dfs(preorder,inorder[:inorder_idx],index_map,offset) 
        root.right = self.dfs(preorder,inorder[inorder_idx+1:],index_map,offset + inorder_idx + 1)
        return root

s = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
s.buildTree(preorder,inorder)