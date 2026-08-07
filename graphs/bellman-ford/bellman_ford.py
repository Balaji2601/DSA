# https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1

class Solution:
    def bellmanFord(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        #code here
        result = [int(1e8)]*V
        result[src] = 0
        
        # relaxing graph V-1 times
        for i in range(1, V):
            for u,v,wt in edges:
                if result[u] != int(1e8) and result[u] + wt < result[v]:
                    result[v] = result[u]+wt
        
        # to detect -ve cycle relaxing one more time
        for u,v,wt in edges:
            if result[u] != int(1e8) and result[u] + wt < result[v]:
                # if it enters this condition then it is a -ve cycle
                return [-1]
        
        return result