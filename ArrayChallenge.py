def ArrayChallenge(arr):
    if len(arr) < 2:
        return 0

    min_price = arr[0]
    max_profit = 0

    for price in arr[1:]:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

    return max_profit

L1 = [44, 30, 24, 32, 35, 30, 40, 38, 15]
print(ArrayChallenge(L1))

L2 = [10, 7, 5, 8, 11, 9]
print(ArrayChallenge(L2))
