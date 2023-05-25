from collections import Counter
import numpy as np

class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        vals = [cnt[k] for k in list(cnt.keys())]
        if np.min(vals) > 1:
            return -1
        else:
            s_list = list(s)
            for i in range(len(s_list)):
                if cnt[s_list[i]] == 1:
                    return i