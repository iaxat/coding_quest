class Solution:
    def maxProfit(self, prices):
        # buy = 0
        # sell = 0
        # profit = []
        # temp = 0

        # le = len(prices)

        # for i in range(0,le):
        #     buy = prices[i]
        #     for j in range(0,le):

        #         if i != j:
        #             sell = prices[j]
        #             if (buy<=sell) and (sell-buy>=0) and j>i:
        #                 # print(buy)
        #                 diff = sell-buy
        #                 # print(diff)
        #                 profit.append(diff)

        # print(profit)
        # return max(profit)

        profit = 0

        le = len(prices)
        for i in range(0,le):
            for j in range(0,le):
                if i!=j and j>i:
                    buy = prices[i]
                    sell = prices[j]
                    if (buy<=sell) and (sell-buy>=0):
                        diff = sell-buy
                        if diff>profit:
                            profit = diff

        print(profit)


prices = [7,1,5,3,6,4]
# 5
sol = Solution()
sol.maxProfit(prices)
