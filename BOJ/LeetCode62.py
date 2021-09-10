import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        s_m = m - 1
        s_n = n - 1

        return math.factorial(s_m + s_n) // (math.factorial(s_m) * math.factorial(s_n))




if __name__=="__main__":
    test=Solution()
    print(test.uniquePaths(7,3))