def characterReplacement(s, k):
    max_length = 0
    max_count = 0
    start = 0
    char_count = [0] * 26
    
    for end in range(len(s)):
        char_count[ord(s[end]) - ord('A')] += 1
        max_count = max(max_count, char_count[ord(s[end]) - ord('A')])
        
        while end - start + 1 - max_count > k:
            char_count[ord(s[start]) - ord('A')] -= 1
            start += 1
        
        max_length = max(max_length, end - start + 1)
    
    return max_length


s = input().upper()  # Convert input to uppercase
k = int(input())

# Calculate and print the result
result = characterReplacement(s, k)
print(result)