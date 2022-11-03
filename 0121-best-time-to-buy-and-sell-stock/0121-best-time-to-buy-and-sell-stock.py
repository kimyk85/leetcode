class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        elif len(prices) == 2:
            return (0 if prices[1] - prices[0] < 0 else prices[1] - prices[0] )
        i = 1
        left = prices[0]
        right = prices[1]
        profit = 0
        while i < len(prices):
            if left > prices[i]:
                left = prices[i]
                if i + 1 == len(prices):
                    break;
                right = prices[i+1]
            elif right < prices[i]:
                right = prices[i]
            if profit < right - left:
                profit = right - left
            i += 1
        return profit