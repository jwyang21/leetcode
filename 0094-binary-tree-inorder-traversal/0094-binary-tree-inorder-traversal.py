# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder: left -> self -> right
        result = []
        
        def dfs(node):
            if node is not None:
                dfs(node.left)
                result.append(node.val)
                dfs(node.right)
        dfs(root)
        return result
    #https://applepick.tistory.com/117
        
        