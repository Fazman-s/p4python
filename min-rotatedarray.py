def findMin(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]

# Read input
nums = list(map(int, input().split()))  # Rotated sorted array

result = findMin(nums)
print(result)
