'''
# trial1
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            probe = numbers[i]
            for j in range(i+1, len(numbers)):
                if numbers[j]==target-probe:
                    return [i+1, j+1]
# trial2
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            mid = (left+right)//2
            if numbers[mid] > target:
                right = mid
            else:
                search_space = numbers[left:right+1]
                for i in range(len(search_space)):
                    probe = search_space[i]
                    for j in range(i+1, len(search_space)):
                        if search_space[j]==target-probe:
                            return [left+i+1, left+j+1]
'''
#trial3
class Solution: #https://sofar-sogood.tistory.com/entry/LeetCode-167-Two-Sum-II-Input-Array-Is-Sorted-Python
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1
        while start < end:
        #while numbers[start]+numbers[end]!=target:
            if numbers[start]+numbers[end] == target:
                return [start+1, end+1]
            elif numbers[start]+numbers[end] > target:
                start = 0
                end -= 1
            else:
                start += 1