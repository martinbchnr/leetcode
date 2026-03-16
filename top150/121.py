from typing import List


# def maxProfit(prices: List[int]) -> int:
#     best_tuple = None
#     best_delta = -float("inf")
#     for b, p_b in enumerate(prices):
#         for s, p_s in enumerate(prices[b:]):
#             delta = p_s - p_b
#             if delta > best_delta:
#                 best_tuple = (b,s+b)
#                 best_delta = delta
    
#     return int(best_delta), best_tuple

def maxProfit(prices: List[int]) -> int:
    """
    Docstring for maxProfit
    
    :param prices: Description
    :type prices: List[int]
    :return: Description
    :rtype: int
    """
    min_price = float("inf")
    max_profit = 0

    min_buy_day = 0
    for d, k in enumerate(prices):
        # set new minimum price
        if k < min_price:
            min_price = k
            min_buy_day = d # not even necessary

        # compute current profit
        profit = k - min_price
        if profit > max_profit:
            max_profit = profit
    
    return max_profit

prices = [7,1,5,3,6,4]

print(maxProfit(prices))