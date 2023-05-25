from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for k in list(cnt.keys()):
            if cnt[k] == 1:
                tmp = k
                break
        return tmp