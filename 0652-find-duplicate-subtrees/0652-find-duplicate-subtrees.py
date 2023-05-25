# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def traverse(node):
            if node:
                node_structure = f'({traverse(node.left)}){node.val}({traverse(node.right)})'
                if node_structure not in list(cnt.keys()):
                    cnt[node_structure] = 0
                cnt[node_structure] += 1
                if cnt[node_structure] == 2:
                    duplicates.append(node)
                return node_structure
            else:
                return ""

        cnt = {}
        duplicates = []
        traverse(root)
        return duplicates