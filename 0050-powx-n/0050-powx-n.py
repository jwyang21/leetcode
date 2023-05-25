class Solution(object):
    def myPow(self, x: float, n: int) -> float:
        if n==1:
            return x
        elif n==0:
            return 1
        elif n < 0:
            return self.myPow(1/x, (-1)*n)
        else:#n>0
            if n % 2 == 0: #거듭제곱의 지수가 2의 배수이면 x를 제곱하고 지수를 2로 나눔 (pow(x^2, n) == pow(x, 2n))
                return self.myPow(x*x, n//2)
            else:
                return x * self.myPow(x, n-1)