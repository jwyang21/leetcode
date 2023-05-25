"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:    return node
        deq = deque([node])
        nodes = {node.val: Node(node.val)}
        
        while deq:
            poped = deq.popleft()
            cur = nodes[poped.val]
            
            for neigh in poped.neighbors:
                if neigh.val not in nodes:
                    nodes[neigh.val] = Node(neigh.val)
                    deq.append(neigh)
                
                cur.neighbors.append(nodes[neigh.val])
            
        return nodes[node.val]#https://sofar-sogood.tistory.com/entry/LeetCode-133-Clone-Graph-Python?category=1016330