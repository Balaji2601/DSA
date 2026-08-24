# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/description/

from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7
        dp = [[(-float("inf"),float("inf"))]*n for _ in range(m)]
        def bound(i,j):
            if 0<=i<m and 0<=j<n:
                return True
            return False

        def solve(i,j):
            if i == m-1 and j == n-1:
                return (grid[i][j], grid[i][j])

            if dp[i][j] != (-float("inf"),float("inf")):
                return dp[i][j]

            maxVal = -float("inf")
            minVal = float("inf")

            # right
            ni = i
            nj = j+1

            if bound(ni,nj):
                rightMax, rightMin = solve(ni,nj)
                maxVal = max(maxVal, grid[i][j]*rightMax, grid[i][j]*rightMin)
                minVal = min(minVal, grid[i][j]*rightMax, grid[i][j]*rightMin)

            # down
            ni = i+1
            nj = j
            if bound(ni,nj):
                downMax, downMin = solve(ni,nj)
                maxVal = max(maxVal, grid[i][j]*downMax, grid[i][j]*downMin)
                minVal = min(minVal, grid[i][j]*downMax, grid[i][j]*downMin)
            dp[i][j] = (maxVal, minVal)
            return (maxVal, minVal)
        
        return solve(0,0)[0] % MOD if solve(0,0)[0] >= 0 else -1