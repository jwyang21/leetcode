class Solution:#https://velog.io/@hrpp1300/LeetCode-162.-Find-Peak-Element
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            middle = (left+right)//2
            if nums[middle]<nums[middle+1]:
                left = middle+1
            else:
                right = middle
        return left