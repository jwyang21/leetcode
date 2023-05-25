class Solution:
    # https://withhamit.tistory.com/586
    # https://kakunblog.tistory.com/19
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        sets = [0] * (len(edges)+1)

        def find(x):
            if sets[x] == 0:
                return x
            else:
                return find(sets[x])
        
        for x,y in edges:
            u = find(x)
            v = find(y)
            if u == v:
                return [x, y]
            else:
                sets[u] = v