import numpy as np

def compute_square(num):
    tmp = 0
    str_num = str(num)
    for k in range(len(str_num)):
        current_digit = int(str_num[k])
        tmp += pow(current_digit, 2)
    return tmp
    
class Solution:
    def isHappy(self, n: int) -> bool:
        results = []
        num_cycles = 10
        for i in range(num_cycles):
            squr = compute_square(n)
            n = squr
            results.append(squr==1)
        return (True in results)