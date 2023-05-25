class Solution:#https://kkminseok.github.io/posts/leetcode_Find_Minimum_in_Rotated_Sorted_Array/
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                ans = nums[i+1]
        return ans