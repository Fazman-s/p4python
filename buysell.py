class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

# Read input
prices = list(map(int, input().split()))  # Stock prices for each day

solution = Solution()
print(solution.maxProfit(prices))
