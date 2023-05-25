import numpy as np
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #basic_int = np.intersect1d(nums1, nums2).tolist()
        nums1_cnt = Counter(nums1)
        nums2_cnt = Counter(nums2)
        
        basic_int = []
        for i in range(len(nums1_cnt)):
            k = list(nums1_cnt.keys())[i]
            if k in list(nums2_cnt.keys()):
                for j in range(min(nums1_cnt[k], nums2_cnt[k])):
                    basic_int.append(k)

        return basic_int