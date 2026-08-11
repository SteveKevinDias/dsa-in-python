class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        hash = {}
        for i in range(0,len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] in hash:
                    repeated = grid[i][j]
                    hash[grid[i][j]] += 1
                else:
                    hash[grid[i][j]] = 1
        n = len(grid)
        missing = 0
        for i in range(1,(n**2)+1):
            if i in hash:
                continue
            else:
                missing = i
        return [repeated, missing]
