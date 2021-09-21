class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[0] * i for i in range(1, numRows + 1)]
        answer[0][0] = 1

        if numRows > 1:
            answer[1][0] = 1
            answer[1][1] = 1

            for i in range(2, numRows):
                for j in range(len(answer[i])):

                    if j == 0:
                        answer[i][j] = answer[i - 1][0]

                    elif j == (len(answer[i]) - 1):
                        answer[i][j] = answer[i - 1][j - 1]

                    else:
                        answer[i][j] = answer[i - 1][j - 1] + answer[i - 1][j]

        return answer






