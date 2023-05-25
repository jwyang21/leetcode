from collections import Counter
import numpy as np

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        keys = list(cnt.keys())
        vals = [cnt[x] for x in keys]
        max_indices = np.argpartition(vals, (-1)*k)[(-1)*k:]
        return np.array(keys)[max_indices].tolist()

        