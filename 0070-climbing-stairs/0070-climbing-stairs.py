class Solution(object):
    num_ways = {}

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            if n not in list(self.num_ways.keys()):
                self.num_ways[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
            return self.num_ways[n]      