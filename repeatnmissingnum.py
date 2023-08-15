def findMissingAndDuplicate(nums):
    n = len(nums)
    
    total_xor = 0
    for i in range(1, n + 1):
        total_xor ^= i

    array_xor = 0
    for num in nums:
        array_xor ^= num
    
    xor_result = total_xor ^ array_xor
    
    # Find the rightmost set bit in xor_result
    rightmost_set_bit = xor_result & -xor_result
    
    a = 0
    b = 0
    for num in nums:
        if num & rightmost_set_bit:
            a ^= num
        else:
            b ^= num
    
    for i in range(1, n + 1):
        if i & rightmost_set_bit:
            a ^= i
        else:
            b ^= i
            
    return [a, b]

# Read input
input_array = list(map(int, input().split()))

result = findMissingAndDuplicate(input_array)
print(result)
