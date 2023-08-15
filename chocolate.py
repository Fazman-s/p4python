def findMinDiff(arr, m):
    n = len(arr)

    if (m == 0 or n == 0):
        return 0

    arr.sort()

    if (n < m):
        return -1

    min_diff = arr[n-1] - arr[0]

    for i in range(len(arr) - m + 1):
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])

    return min_diff

# Read input
m = int(input())  # Number of students
arr = list(map(int, input().split()))  # List of sizes of packets

print("Minimum difference is", findMinDiff(arr, m))
