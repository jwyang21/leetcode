from collections import Counter
import numpy as np

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        v = []
        _ = np.array([cnt[k] >= 2 for k in list(cnt.keys())]).sum()
        return _