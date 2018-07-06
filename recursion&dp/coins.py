def changes(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for j in range(coin, amount + 1):
            ways[j] += ways[j - coin]
    return ways[amount]


def coins(amount):
    if amount < 0:
        return 0

    if amount == 0:
        return 1

    return coins(amount - 1) + coins(amount - 5) + coins(amount - 10) + coins(amount - 25)


print(changes(6, [1, 5, 10, 25]))
print(coins(6))