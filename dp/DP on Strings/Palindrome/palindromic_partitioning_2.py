# https://leetcode.com/problems/palindrome-partitioning-ii/description/

# recursion
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if s == s[::-1]:
            return 0

        def solve(i,j):
            if i >= j:
                return 0
            if s[i:j+1] == s[i:j+1][::-1]:
                return 0
            
            ans = float("inf")

            for k in range(i, j):
                ans = min(1+solve(i,k)+solve(k+1,j),ans)
            
            return ans
        
        return solve(0,n-1)


# recursion + memoization
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if s == s[::-1]:
            return 0

        dp = [[-1]*(n+1) for _ in range(n+1)]
        def solve(i,j):
            if i >= j:
                return 0
            if s[i:j+1] == s[i:j+1][::-1]:
                dp[i][j] = 0
                return dp[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            
            ans = float("inf")

            for k in range(i, j):
                ans = min(1+solve(i,k)+solve(k+1,j),ans)
            
            dp[i][j] = ans
            return ans
        
        return solve(0,n-1)

# recursion + memoization with palidrome check with bottom up(blue print)
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if s == s[::-1]:
            return 0
        
        dp1 = [[False]*(n+1) for _ in range(n+1)]

        for L in range(1,n+1):
            for i in range(n-L+1):
                j = i+L-1
                if i == j:
                    dp1[i][j] = True
                elif i+1 == j:
                    dp1[i][j] = s[i] == s[j]
                else:
                    dp1[i][j] = s[i] == s[j] and dp1[i+1][j-1]
        

        dp = [[-1]*(n+1) for _ in range(n+1)]
        def solve(i,j):
            if i >= j:
                return 0
            if dp1[i][j]:
                dp[i][j] = 0
                return dp[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            
            ans = float("inf")

            for k in range(i, j):
                ans = min(1+solve(i,k)+solve(k+1,j),ans)
            
            dp[i][j] = ans
            return ans
        
        return solve(0,n-1)