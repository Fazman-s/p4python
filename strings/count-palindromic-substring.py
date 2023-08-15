class Solution:

    def countPS(self, string):

        def subs(i, j, strg):
            if i > j:
                return 0

            if i == j:
                return 1

            if dp[i][j] != -1:
                return dp[i][j]

            if strg[i] == strg[j]:
                dp[i][j] = subs(i + 1, j, strg) + subs(i, j - 1, strg) + 1
            else:
                dp[i][j] = subs(i + 1, j, strg) + subs(i, j - 1, strg) - subs(i + 1, j - 1, strg)

            return dp[i][j]    

        n = len(string)
        MOD = 10**9 + 7
        dp = [[-1] * (n) for i in range(n)]
        ans = subs(0, n - 1, string)
        return ans % MOD

# Example
if __name__ == "__main__":
    solution = Solution()
    input_str = input().strip()
    result = solution.countPS(input_str)
    print(result)
