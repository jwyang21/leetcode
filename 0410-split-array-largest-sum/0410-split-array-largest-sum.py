'''
#trial1
# https://velog.io/@apparatus1/Leetcode-410.Split-Array-Largest-Sum
class Solution:
    def canSplitNums(self, nums, max_, m):
        count, sum_ = 1, 0
        for num in nums:
            sum_ += num
            if sum_ > max_:
                sum_ = num
                count += 1
            if count>m:
                return False
        return True
    
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        mid = 0
        while left < right:
            mid = (left+right)//2
            if self.canSplitNums(nums, mid, mid):
                right = mid
            else:
                left = mid+1
        return left


# trial2 (https://ohgym.tistory.com/87)
class Solution:
    def splitable(self, nums, m, maxValue):
        cur = 0
        for num in nums:
            if num > maxValue: return False
            cur += num
            if cur > maxValue:
                if --m==0: return False
                else: curr = num
        return True
    
    def splitArray(self, nums: List[int], k: int) -> int:
        s = sum(nums)
        l = 0
        r = s
        while l != r-1:
            mid = int(l + ((r-l)/2))
            if self.splitable(nums, k, mid):
                r = mid
            else:
                l = mid
        return r

# trial3 (https://bcp0109.tistory.com/246)
class Solution:
    def cansplit(self, targetSum, nums, m):
        cnt, s = 1, 0
        for num in nums:
            s += num
        if s > targetSum:
            cnt += 1
            s = num
            if cnt > m: return False
        return True
    
    def splitArray(self, nums: List[int], k: int) -> int:
        minSum, maxSum = 0, 0
        
        for num in nums:
            minSum = max(minSum, num)
            maxSum += num
        
        lo, hi = minSum, maxSum
        
        while lo <= hi:
            #mid = (lo+hi)//2
            mid = int(lo + ((hi - lo) / 2))
            if self.cansplit(mid, nums, k):
                hi = mid-1
            else:
                lo = id + 1
        return lo
'''
#trial4
# Java to Python by kalkicode.com
import math
class Solution(object) :
    
    def  splitArray(self, nums,  m) :
        minSum = 0
        maxSum = 0
        for num in nums :
            minSum = max(minSum,num)
            maxSum += num
        lo = minSum
        hi = maxSum
        while (lo <= hi) :
            mid = lo + int((hi - lo) / 2)
            if (self.canSplit(mid, nums, m)) :
                hi = mid - 1
            else :
                lo = mid + 1
        return lo
    
    def  canSplit(self, targetSum,  nums,  m) :
        count = 1
        s = 0
        for num in nums :
            s += num
            if (s > targetSum) :
                count += 1
                s = num
                if (count > m) :
                    return False
        return True