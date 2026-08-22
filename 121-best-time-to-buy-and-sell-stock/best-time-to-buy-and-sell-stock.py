class Solution(object):
    def maxProfit(self, prices):
        buy_price=prices[0]
        profit=0
        for price in (prices):
            if price < buy_price:
                buy_price = price
            else:
                current_profit = price - buy_price
                profit = max(profit,current_profit)
        return profit
