import numpy as np
from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        mat = np.array(board)
        
        
        all_results = []
        # check whether each row is valid
        for i in range(mat.shape[0]):
            row_cnt = Counter(mat[i,:].flatten())
            for x in list(row_cnt.keys()):
                if x != "." and row_cnt[x] >= 2:
                    #all_results.append(False)
                    return False
                
        # check whether each column is valid
        for i in range(mat.shape[1]):
            col_cnt = Counter(mat[:,i].flatten())
            for x in list(col_cnt.keys()):
                if x != "." and col_cnt[x] >= 2:
                    #all_results.append(False)
                    return False
                
        # check whether each subbox is valid
        for i in range(3):#row index
            for j in range(3):#column index
                current_sub = mat[i*3:(i+1)*3,j*3:(j+1)*3].flatten()
                sub_cnt = Counter(current_sub)
                for x in list(sub_cnt.keys()):
                    if x != "." and sub_cnt[x] >= 2:
                        #all_results.append(False)
                        return False
                    
        return True