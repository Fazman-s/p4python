def longestPrefixSuffix(s):
    n = len(s)
    lps = [0] * n
    length = 0
    
    i = 1
    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps[n - 1]

if __name__ == "__main__":
    s = input().strip()
    result = longestPrefixSuffix(s)
    print(result)
