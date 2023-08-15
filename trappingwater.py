class Solution:
    def trap(self, height):
        left, right = 0, len(height) - 1
        lmax, rmax = height[left], height[right]
        water = 0
        while left < right:
            lmax, rmax = max(lmax, height[left]), max(rmax, height[right])
            if lmax <= rmax:
                water += lmax - height[left]
                left += 1
            else:
                water += rmax - height[right]
                right -= 1
        return water

# Read input
height = list(map(int, input().split()))  # List of height values

solution = Solution()
print(solution.trap(height))

