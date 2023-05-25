class Solution(object):
    dp = {}
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            if n not in list(self.dp.keys()):
                self.dp[n] = self.fib(n-1)+self.fib(n-2)
            return self.dp[n]
        
'''
def fib(self, n: int) -> int:
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return self.fib(n-1)+self.fib(n-2)
'''