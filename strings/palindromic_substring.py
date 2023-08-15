class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    cnt += 1
        return cnt


s = input()

solution = Solution()
result = solution.countSubstrings(s)
print(result)