def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSelect(arr, low, high, k):
    if low <= high:
        pivot_index = partition(arr, low, high)

        if pivot_index == k - 1:
            return arr[pivot_index]
        elif pivot_index < k - 1:
            return quickSelect(arr, pivot_index + 1, high, k)
        else:
            return quickSelect(arr, low, pivot_index - 1, k)

def kthSmallest(arr, l, r, k):
    return quickSelect(arr, l, r, k)

# Taking input and calling kthSmallest function
if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    K = int(input())
    
    result = kthSmallest(arr, 0, N - 1, K)
    print(result)
