class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        all_jewels = list(jewels)
        cnt = 0
        for x in list(stones):
            if x in all_jewels:
                cnt += 1 
        return cnt