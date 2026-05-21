"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        h_map={}

        def dfs(node):
            if node in h_map:
                return h_map[node]
            
            copy=Node(node.val)
            h_map[node]=copy
            for nb in node.neighbors:
                copy.neighbors.append(dfs(nb))
            
            return copy
        
        return dfs(node)
            