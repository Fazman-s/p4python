class Solution:
    def nextPermutation(self, nums):
        k = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                k = i
                temp = nums[i]
                break
        if k == -1:
            nums.sort()
            return

        l = -1
        for i in range(len(nums) - 1, k - 1, -1):
            if temp < nums[i]:
                l = i
                break
        
        nums[k] = nums[l]
        nums[l] = temp

        for i in range(k + 1, (k + 1 + len(nums)) // 2):
            t = nums[i]
            nums[i] = nums[len(nums) - 1 - (i - k - 1)]
            nums[len(nums) - 1 - (i - k - 1)] = t

# Create an instance of the Solution class
solution = Solution()

# Read input from standard input
nums = list(map(int, input().split()))

# Call the nextPermutation method and modify the input list in-place
solution.nextPermutation(nums)

# Print the modified list
print(nums)