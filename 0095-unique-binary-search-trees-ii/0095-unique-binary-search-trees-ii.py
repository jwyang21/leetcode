# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://dxmahata.gitbooks.io/leetcode-python-solutions/content/unique_binary_search_trees_ii.html
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # make unique BSTs from the nodes having value of 1, 2, ..., n
        if n == 0:
            return []
        else:
            return self.tree_constructor(1, n)
        
    def tree_constructor(self, m:int, n:int):
        # m: start
        # n: end
        results = []
        if m > n:
            results.append(None)
            return results #start > end. No possible BST
        else:
            for i in range(m, n+1):
                l = self.tree_constructor(m, i-1) # find all possible left subtrees
                r = self.tree_constructor(i+1, n) # find all possible right subtrees
                for left_tree in l:
                    for right_tree in r:
                        # for every combination of available left and right subtrees:
                        curr_node = TreeNode(i)
                        curr_node.left = left_tree
                        curr_node.right = right_tree
                        results.append(curr_node)
            return results
        