import copy
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        answer = copy.deepcopy(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    answer[i][j] = grid[i][j]
                else:
                    if i > 0 and j > 0:
                        answer[i][j] = min(answer[i][j - 1] + answer[i][j], answer[i - 1][j] + grid[i][j])

                    elif i == 0 and j > 0:
                        answer[i][j] = answer[i][j - 1] + grid[i][j]

                    elif j == 0:
                        answer[i][j] = answer[i - 1][j] + grid[i][j]

        return answer[n - 1][m - 1]


