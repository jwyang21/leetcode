class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        listA = collections.defaultdict(int)
        listB = collections.defaultdict(int)
        
        for i in A:
            for j in B:
                listA[i+j] += 1
        for i in C:
            for j in D:
                listB[i+j] += 1
                
        count = 0
        
        for i in listA:
            if -i in listB:
                count += listA[i] * listB[-i]
                    
        return count