#Transform One String to Another using Minimum Number of Given Operation
def transform(A, B):
    if len(A) != len(B):
        return -1
    
    m = {}
    n = len(A)
    for i in range(n):
        if A[i] in m:
            m[A[i]] += 1
        else:
            m[A[i]] = 1
    
    for i in range(n):
        if B[i] in m:
            m[B[i]] -= 1
    
    for key in m:
        if m[key] != 0:
            return -1
    
    i, j = n - 1, n - 1
    res = 0
    while i >= 0 and j >= 0:
        while i >= 0 and A[i] != B[j]:
            res += 1
            i -= 1
        i -= 1
        j -= 1
    
    return res

# Example
if __name__ == "__main__":
    A = input().strip()
    B = input().strip()
    result = transform(A, B)
    print("Minimum number of operations required is", result)
