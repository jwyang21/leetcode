from collections import Counter
import numpy as np

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        val_list = list(cnt.values())
        target_ind = np.argpartition(val_list, -1)[-1]
        key_list = list(cnt.keys())
        return key_list[target_ind]
        