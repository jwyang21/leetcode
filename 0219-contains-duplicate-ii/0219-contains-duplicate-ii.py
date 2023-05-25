import numpy as np
from collections import Counter

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_cnt = Counter(nums)
        
        duplicates = []
        for a in list(nums_cnt.keys()):
            if nums_cnt[a] > 1 and a not in duplicates:
                duplicates.append(a)
        
        #all_results = []
        
        for i in range(len(duplicates)):
            current_duplicate = duplicates[i]
            current_duplicate_inds = []
            for j in range(len(nums)):
                if nums[j] == current_duplicate:
                    current_duplicate_inds.append(j)
            for j in range(len(current_duplicate_inds)-1):
                gap = abs(current_duplicate_inds[j+1] - current_duplicate_inds[j])
                if gap <= k:
                    return True