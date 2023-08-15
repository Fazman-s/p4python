import heapq

def findKthLargest(nums, k):
    p = []
    for x in nums:
        heapq.heappush(p, x)
        if len(p) > k:
            heapq.heappop(p)
    return p[0]

# Read input
nums = list(map(int, input().split()))  # List of integers
k = int(input())  # Value of k

result = findKthLargest(nums, k)
print(result)
