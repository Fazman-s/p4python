def nextPermutation(N, arr):
    i = N - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    
    if i == -1:
        arr.reverse()
        return arr
    
    j = N - 1
    while arr[j] <= arr[i]:
        j -= 1
    
    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = arr[i + 1:][::-1]
    
    return arr

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    result = nextPermutation(N, arr)
    print(*result)
