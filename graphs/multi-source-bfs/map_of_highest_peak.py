from collections import deque
from typing import List
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        q = deque()
        heights = [[-1]*n for _ in range(m)]
        directions = [(1,0), (0,-1), (-1,0), (0,1)]
        visited = [[False]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append((i,j))
                    heights[i][j] = 0
                    visited[i][j] = True
        
        def bound(i,j):
            if 0<=i<m and 0<=j<n and not visited[i][j] and isWater[i][j] == 0:
                return True
            return False

        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                heights[i][j] = level

                for di, dj in directions:
                    ni = i+di
                    nj = j+dj

                    if bound(ni, nj):
                        q.append((ni, nj))
                        visited[ni][nj] = True

            if q:
                level += 1
        
        return heights
