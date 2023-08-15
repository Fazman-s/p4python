def is_valid(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in brackets.values():
            
            stack.append(char)
        elif char in brackets.keys():
            
            if not stack or stack[-1] != brackets[char]:
                return "NO"
            stack.pop()
        else:
            
            continue
    
   
    return "YES" if len(stack) == 0 else "NO"


s = input()


print(is_valid(s))




"""
def valid(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

s = input()

if valid(s):
    print('Yes')
else:
    print('No')
"""