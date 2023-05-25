class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i:int ,j:int):
            image[i][j] = color
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and image[x][y]==f_color:
                    dfs(x,y)
        f_color, m, n = image[sr][sc], len(image), len(image[0])
        if f_color != color:
            dfs(sr, sc)
        return image
            
        