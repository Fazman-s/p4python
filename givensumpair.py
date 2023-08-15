def hasPairWithSum(arr, X):
    n = len(arr)
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            break
    
    l = (i + 1) % n
    r = i
    
    while l != r:
        curr_sum = arr[l] + arr[r]
        
        if curr_sum == X:
            return True
        elif curr_sum < X:
            l = (l + 1) % n
        else:
            r = (n + r - 1) % n
    
    return False

# Read input
arr = list(map(int, input().split()))  # List of integers
X = int(input())  # Target sum

result = hasPairWithSum(arr, X)
print(result)
