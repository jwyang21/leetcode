class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        
        while left <= right:
            mid = (left+right)//2
            tmp = mid * mid
            tmp_ = (mid+1)*(mid+1)
            if tmp <= x and x < tmp_:
                return mid
            else:
                if tmp < x:
                    left = mid + 1
                else:
                    right = mid -1  
            
        