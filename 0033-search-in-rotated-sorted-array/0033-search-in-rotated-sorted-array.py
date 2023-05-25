class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None:
            return -1
        else:
            min_ = min(nums)
            if nums.index(min_)!=0:
                pivot = nums.index(min_)
                new_nums = []
                smaller_nums = nums[pivot:]
                bigger_nums = nums[:pivot]
                for x in smaller_nums:
                    new_nums.append(x)
                for x in bigger_nums:
                    new_nums.append(x)
            else:
                pivot = 0
                new_nums = nums

            left, right = 0, len(nums)
            while left <= right:
                middle = (left+right)//2
                if middle >= len(nums):
                    return -1
                else:
                    #print(left, right, middle)
                    if target==new_nums[middle]:
                        return (middle+pivot)%len(nums)
                    elif target > new_nums[middle]:
                        left = middle + 1
                    else: #target < new_nums[middle]:
                        right = middle - 1
            return -1