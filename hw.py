import timeit


coins = [50, 25, 10, 5, 2, 1]
sum = 113


# 1. Функція жадібного алгоритму find_coins_greedy
def find_coins_greedy(coins, sum):
    result = {}
    for coin in coins:
        coin_count = sum // coin
        sum = sum - coin_count * coin
        if coin_count > 0:
            result[coin] = coin_count
    return result


print(find_coins_greedy(coins, sum))


# 2. Функція динамічного програмування find_min_coins
def find_min_coins(coins, sum):
    dp = [float('inf')] * (sum + 1)
    dp[0] = 0
    sum_coin = {}
    result = {}

    for s in range(1, sum + 1):
        for coin in coins:
            if coin <= s and dp[s - coin] + 1 < dp[s]:
                dp[s] = dp[s - coin] + 1
                sum_coin[s] = coin

    s = sum
    while s > 0:
        if sum_coin[s] in result:
            result[sum_coin[s]] = result[sum_coin[s]] + 1
        else:
            result[sum_coin[s]] = 1
        s -= sum_coin[s]
    return result


print(find_min_coins(coins, sum))

time = timeit.timeit(lambda: find_coins_greedy(coins, 157562), number=200)
print(
    f'# Функція жадібного алгоритму. time = {time} ')
print(27.646/0.000146)
time = timeit.timeit(lambda: find_min_coins(coins, 157562), number=200)
print(
    f'# Функція динамічного програмування. time = {time} ')
