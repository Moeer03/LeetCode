from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = [[0 for _ in range(n - 2)] for _ in range(n - 2)]
        
        for i in range(n - 2):
            for j in range(n - 2):
                max_val = 0
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        max_val = max(max_val, grid[x][y])
                result[i][j] = max_val
        
        return result
