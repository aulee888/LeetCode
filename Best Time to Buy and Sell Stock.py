class Solution:
    def maxProfit(self, prices):
        """Brute force"""
        n = len(prices)
        max_profit = 0

        for buy in range(n - 1):
            curr_profit = 0

            for sell in range(buy + 1, n):
                # print(f'{prices[buy]} & {prices[sell]} = {prices[sell] - prices[buy]}')

                if prices[sell] - prices[buy] > curr_profit:  # Implicitly says that prices[sell] > prices[buy]
                    curr_profit = prices[sell] - prices[buy]

            if curr_profit > max_profit:
                max_profit = curr_profit

        return max_profit

    def maxProfit2(self, prices):
        """Single pass"""
        n = len(prices)
        max_profit = 0
        min_price = 2**64 - 1  # A reasonably large number

        for i in range(n):
            if prices[i] < min_price:
                min_price = prices[i]

            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit
