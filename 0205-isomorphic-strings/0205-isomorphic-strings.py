from collections import Counter
import numpy as np
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_cnt = Counter(s)
        t_cnt = Counter(t)
        
        # s와 t에서 unique alphabet의 개수가 같다면
        if len(s_cnt) == len(t_cnt):
            s_keys = list(s_cnt.keys())
            t_keys = list(t_cnt.keys())
            
            s_vals = [s_cnt[k] for k in list(s_cnt.keys())] #ex: [1, 4, 2, 3]
            t_vals = [t_cnt[k] for k in list(t_cnt.keys())] #ex: [2, 1, 3, 4]

            # s_vals, t_vals를 오름차순으로 정렬한 것의 index
            s_arg_ind = np.argsort(s_vals) 
            t_arg_ind = np.argsort(t_vals)
            

            
            s_keys2 = [s_keys[i] for i in s_arg_ind]
            t_keys2 = [t_keys[i] for i in t_arg_ind]
            
            change_st = {}
            change_ts = {}
            
            for i in range(len(s_keys2)):
                change_st[s_keys2[i]] = t_keys2[i]
                change_ts[t_keys2[i]] = s_keys2[i]
                
            s2 = list(s)
            #t2 = list(t)
            
            for i in range(len(s2)):
                s2[i] = change_st[s2[i]]
                #t2[i] = change_ts[t2[i]]
                
            s2 = ''.join(s2)
            #t2 = ''.join(t2)
            return s2 == t