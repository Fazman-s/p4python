def is_valid(s):
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return False
    return balance == 0

def rm_invalid_par(s):
    queue = [s]
    visited = set()
    valid_strings = []

    while queue:
        current = queue.pop(0)
        
        if is_valid(current):
            valid_strings.append(current)
            continue
        
        if not valid_strings:
            for i in range(len(current)):
                if current[i] in '()':
                    new_string = current[:i] + current[i+1:]
                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append(new_string)
    
    return valid_strings

p = input()

result = rm_invalid_par(p)
for valid_string in result:
    print(valid_string)
