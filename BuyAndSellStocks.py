def findMaxProfit(prices):
    minPrice = prices[0]
    maxProfit = 0

    for price in prices:
        minPrice = min(minPrice, price)
        diff = price - minPrice
        maxProfit = max(maxProfit, diff)

    return maxProfit


if __name__ == "__main__":
    A = list(map(int, input().strip('[').strip(']').split(',')))

    print(findMaxProfit(A))
    