class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        #calculate minimum value about column 0
        for i in range(m-1):
            grid[i+1][0] += grid[i][0]
        #calculate minimum value about row 0    
        for j in range(n-1):
            grid[0][j+1] += grid[0][j]
        #Find minimum summation by choosing minumum summation of last grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])
        #Result
        return grid[m-1][n-1]