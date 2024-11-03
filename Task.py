import timeit
import heapq

# Жадібний алгоритм
def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

# Алгоритм динамічного програмування
def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

amount = 113
coins = [50, 25, 10, 5, 2, 1]
print("Жадібний алгоритм:", find_coins_greedy(amount, coins))
print("Динамічне програмування:", find_min_coins(amount, coins))

greedy_time = timeit.timeit(lambda: find_coins_greedy(amount, coins), number=1000)
dp_time = timeit.timeit(lambda: find_min_coins(amount, coins), number=1000)
print("Час виконання жадібного алгоритму:", greedy_time)
print("Час виконання динамічного програмування:", dp_time)
