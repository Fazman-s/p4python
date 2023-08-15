def isMatch(wild, pattern):
    m, n = len(wild), len(pattern)
    
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if wild[i - 1] == pattern[j - 1] or wild[i - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif wild[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    
    return dp[m][n]

if __name__ == "__main__":
    wild = input().strip()
    pattern = input().strip()
    result = isMatch(wild, pattern)
    print("Yes" if result else "No")
