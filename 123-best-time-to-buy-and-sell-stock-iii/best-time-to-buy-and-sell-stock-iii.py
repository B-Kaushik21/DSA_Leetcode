class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_1=-prices[0]
        sell_1=0
        buy_2=-prices[0]
        sell_2=0
        for i in range(1,len(prices)):
            price=prices[i]
            buy_1=max(buy_1,-price)
            sell_1=max(sell_1,buy_1+price)
            buy_2=max(buy_2,sell_1-price)
            sell_2=max(sell_2,buy_2+price)
        return sell_2