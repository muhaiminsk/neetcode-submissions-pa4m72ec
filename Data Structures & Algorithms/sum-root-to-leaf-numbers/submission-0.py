# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(cur, curSum):
            if not cur:
                return 0
            curSum = curSum*10+cur.val
            if not cur.left and not cur.right:
                return curSum
            return dfs(cur.left, curSum) + dfs(cur.right, curSum)
        return dfs(root, 0)
            
        