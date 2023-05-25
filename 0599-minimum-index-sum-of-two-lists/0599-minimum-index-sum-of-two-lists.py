import numpy as np

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        int_ = np.intersect1d(list1, list2)
        if len(int_) == 1:
            return int_
        else:
            indsum = {}
            vals = []
            for x in int_:
                if x not in list(indsum.keys()):
                    indsum[x] = 0
                indsum[x] += list1.index(x)
                indsum[x] += list2.index(x)
                vals.append(list1.index(x) + list2.index(x))
            m = np.min(vals)
            #min_cnt = 0
            min_items = []
            for i in range(len(indsum)):
                k = list(indsum.keys())[i]
                v = indsum[k]
                if v == m:
                    min_items.append(k)
            return min_items