from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_list = []
        for start_position in range(len(prices)):
            price = prices[start_position]

            for i in range(start_position + 1, len(prices)):
                if price < prices[i]:

                    profit_list.append(prices[i] - price)

        return max(profit_list) if profit_list else 0



if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))
    print(solution.maxProfit([7,6,4,3,1]))
