class Solution:
    ans = -1
    tmp = 0
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        else:
            left, right = 0, len(nums)
            mid = (left+right)//2     

            while left < right:
                if nums[mid]==target:
                    self.tmp += mid
                    self.ans = self.tmp
                    return self.ans
                    #return mid
                else:
                    if nums[mid] <= target:
                        self.tmp += mid
                        left = mid                    
                        return self.search(nums[left:right], target)
                    else:                    
                        right = mid
                        return self.search(nums[left:right], target)
            return self.ans