'''
# trial1
class Solution:
    hashmap = []
    def smallestDistancePair(self, nums, k):
        nums = sorted(nums)
        if nums[0]==nums[-1]:
            return 0
        else:
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    abs_dist = abs(nums[i] - nums[j])
                    if abs_dist not in self.hashmap:
                        self.hashmap.append(abs_dist)
            #print(sorted(self.hashmap))
            return sorted(self.hashmap)[k-1]
'''
# problem : https://leetcode.com/problems/find-k-th-smallest-pair-distance/
# time complexity : O(NlogN + NlogM)
'''
class Solution:
    def count_(self, mid: int, nums:List[int]) -> int:
        # nums 안에서 distance <= mid를 만족하는 element pair들의 총 개수 반환
        highInd = 1
        cnt = 0
        for lowInd in range(len(nums)):
            while highInd < len(nums) and nums[highInd]-nums[lowInd]<mid:
                highInd += 1
            cnt += max(0, (highInd-lowInd-1))
        return cnt
    
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        high = nums[-1] - nums[0] #최대 distance
        low = 0
        while low < high:
            mid = (high+low)//2
            cnt = self.count_(mid, nums)
            if cnt >= k:
                high = mid
            else:
                low = mid+1
        return low
'''
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count(mid: int):
            # nums 안에서 distance <= mid를 만족하는 element pair들의 총 개수 반환
            highInd = 1
            cnt = 0
            for lowInd in range(len(nums)):
                while highInd < len(nums) and nums[highInd] - nums[lowInd] <= mid:
                    highInd += 1
                cnt += max(0, (highInd - lowInd - 1))
            return cnt

        nums.sort()
        high = nums[-1] - nums[0] #최대 distance
        low = 0
        while low < high:
            mid = int((high + low)/2)
            cnt = count(mid)
            if cnt >= k:
                high = mid # search space를 왼쪽 절반으로 줄임. 
            else:#cnt<k
                low = mid + 1
        return low