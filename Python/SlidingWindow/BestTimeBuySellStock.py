class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ''' Time Limit Exceeded
        max_profit = 0
        for i, pricei in enumerate(prices):
            for j, pricej in enumerate(prices[i+1:]):
                if pricej-pricei > max_profit:
                    max_profit = pricej-pricei
        return max_profit
        '''
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
