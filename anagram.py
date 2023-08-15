def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    s_freq = [0] * 26
    t_freq = [0] * 26
    
    for char in s:
        s_freq[ord(char) - ord('a')] += 1
    
    for char in t:
        t_freq[ord(char) - ord('a')] += 1
    
    return s_freq == t_freq

# Input
s = input().strip()
t = input().strip()

# Output
if is_anagram(s, t):
    print("true")
else:
    print("false")
