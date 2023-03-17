class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxprice = -1
        minprice = -1

        for price in prices:
            if maxprice > price and maxprice >= 0 and minprice >= 0:
                profit += (maxprice - minprice)
                maxprice = price
                minprice = price
            else:
                if maxprice == -1:
                    maxprice = price
                else:
                    maxprice = max(maxprice, price)
                if minprice == -1:
                    minprice = price
                else:
                    minprice = min(minprice, price)
        profit += (maxprice - minprice)
        return profit
        