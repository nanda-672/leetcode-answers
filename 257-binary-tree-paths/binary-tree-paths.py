# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans, sol = [], [str(root.val)]
        def backtrack(root):
            if not(root.left or root.right):
                print(sol)
                ans.append("->".join(sol))
                return
            
            if root.left:
                cur = root.left
                sol.append(str(cur.val))
                backtrack(cur)
                sol.pop()

            if root.right:
                cur = root.right
                sol.append(str(cur.val))
                backtrack(cur)
                sol.pop()

        backtrack(root)
        return ans
        