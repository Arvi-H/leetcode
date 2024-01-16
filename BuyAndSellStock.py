def maxProfit(prices):
    maxProfit = 0
    smallestPrice = float('inf')

    for i in prices:
        if i < smallestPrice:
            smallestPrice = i

        if i - smallestPrice > maxProfit:
            maxProfit = i - smallestPrice

    return maxProfit
    
print("Maximum Profit:", maxProfit([7, 1, 5, 3, 6, 4]))