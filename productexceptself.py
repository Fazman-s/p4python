def productExceptSelf(nums):
    n = len(nums)
    
    # Initialize the output array
    answer = [1] * n
    
    # Calculate prefix products
    prefix_product = 1
    for i in range(n):
        answer[i] *= prefix_product
        prefix_product *= nums[i]
    
    # Calculate suffix products and multiply with prefix products
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix_product
        suffix_product *= nums[i]
    
    return answer

# Read input
nums = list(map(int, input().split()))  # List of integers

result = productExceptSelf(nums)
print(result)
