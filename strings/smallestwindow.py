#string containing all the characters as the other string
class Solution:
    def smallestWindow(self, s, t):
        if t == "":
            return ""
        
        countT, window = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT)

        result = [-1, -1]
        resLen = float("infinity")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    result = [l, r]
                    resLen = (r - l + 1)

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = result
        return s[l:r + 1] if resLen != float("infinity") else "-1"

if __name__ == "__main__":
    solution = Solution()
    s = input().strip()
    t = input().strip()
    result = solution.smallestWindow(s, t)
    print(result)
