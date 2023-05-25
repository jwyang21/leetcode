class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        # 큐는 리스트로 사용
        q = []
        m = len(grid)
        n = len(grid[0])
        # BFS 방문 배열 생성
        visited = [[0] * n for _ in range(m)]
        dir = [ #dir의 각 element의 첫번째 혹은 두번째 값을 현재 위치의 x 및 y축좌표에 더함으로써 상하좌우 방향으로
            [1,0],  #한 칸 이동 가능. 
            [0,1],
            [-1,0],
            [0,-1]
        ]
        # 모든 칸을 확인해서 시작점으로 잡아야함
        for y in range(m):
            for x in range(n):
            	# 섬이 아니거나, 방문했다면 스킵
                if grid[y][x] == "0":#땅이 아님
                    continue
                if visited[y][x] == 1: #이미 방문했음. 
                    continue
                q.append([y, x]) #땅이고, 이미 방문하지 않았음. 따라서 count를 1 증가시킴. 
                visited[y][x] = 1 #지금 방문했으므로 방문 완료 표시. 
                # BFS 시작이라면 그곳은 방문하지 않은 섬, 카운트 시작
                ans += 1 #섬 카운트 1 증가. 
                # BFS 시작
                while(q):
                    curNode = q.pop()
                    for i in range(4):
                        nxtY = curNode[0] + dir[i][0]
                        nxtX = curNode[1] + dir[i][1]
                        if nxtY >= m or nxtX >=n or nxtY < 0 or nxtX < 0: #valid index가 아닌 경우
                            continue
                        if visited[nxtY][nxtX] == 1: #이미 방문했을 경우
                            continue
                        if grid[nxtY][nxtX] == "0":#물인 경우
                            continue
                        visited[nxtY][nxtX] = 1#방문완료 표시.
                        q.append([nxtY,nxtX])
        return ans