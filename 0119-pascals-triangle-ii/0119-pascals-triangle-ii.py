'''
def pascal_triangle(row_index, col_index):
    if col_index == 0:
        return 1
    elif row_index == col_index:
        return 1
    else:
        return pascal_triangle(row_index-1, col_index-1) + pascal_triangle(row_index-1, col_index)
'''
# https://oneteveryday.tistory.com/219
class Solution(object):
    def getRow(self, rowIndex):
        row = [1]
        
        for i in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
            
        return row
        