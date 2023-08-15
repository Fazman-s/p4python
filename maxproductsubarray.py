def maxProduct(nums):
    n = len(nums)
    max_product = nums[0]
    min_product = nums[0]
    result = max_product
    
    for i in range(1, n):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product)
    
    return result

# Read input
nums = list(map(int, input().split()))  # List of integers

result = maxProduct(nums)
print(result)
