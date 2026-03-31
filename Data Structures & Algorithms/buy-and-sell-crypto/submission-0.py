class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        max_sell_prices = [-1]*len(prices)
        i = len(prices)-2
        while i >= 0:
            max_sell_prices[i] = max(max_sell_prices[i+1], prices[i+1])
            i -= 1
        
        # For every day that you can buy, compare if you can sell at a
        # better prices than the day using max_sell_prices
        # If yes, update the global max
        for i in range(0, len(prices)-1):
            if prices[i] < max_sell_prices[i]:
                max_profit = max(max_profit, max_sell_prices[i]-prices[i])
        
        return max_profit if max_profit >= 0 else 0


"""
[10,1,5,6,7,1]
[ 7,7,7,7,1,-1]

Bf:
buy at i:
    in range i+1:
        find a price > @i
        update max profit (incl 0)


[10,9,8]
[ 9,8,-1]

if max is -1: return 0
"""