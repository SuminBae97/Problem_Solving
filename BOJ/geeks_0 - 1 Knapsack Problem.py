class Solution:

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):

        wt.insert(0, 0)
        val.insert(0, 0)

        bags = [[0, 0]]

        for i in range(1, n + 1):
            bags.append([wt[i], val[i]])

        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, W + 1):
                weights = bags[i][0]
                values = bags[i][1]

                if j < weights:
                    dp[i][j] = dp[i - 1][j]

                else:
                    dp[i][j] = max(dp[i - 1][j - weights] + values, dp[i - 1][j])

        return dp[n][W]
