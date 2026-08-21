# https://leetcode.com/problems/longest-common-subsequence/description/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[-1]*(n2+1) for _ in range(n1+1)]

        # i iterated on text1, j iterated on text2
        def solve(i,j):
            if i >= n1 or j >= n2:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            choose,skip1,skip2 = 0,0,0

            # checking every index with value, if both are equal then choose it and move to next index in both
            if text1[i] == text2[j]:
                choose = 1+solve(i+1,j+1)
            # if not matched then we only skip i for 1 time and find answer and only skip j for 1 time 
            else:
                skip1 = solve(i+1,j)
                skip2 = solve(i,j+1)
            
            dp[i][j] = max(choose, skip1, skip2)
            return max(choose, skip1, skip2)

        return solve(0,0)