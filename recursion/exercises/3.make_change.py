def make_change(coin_value_list, change, min_coins):
    for cent in range(change + 1):
        coin_count = cent
        for j in [c for c in coin_value_list if c <= cent]:
            coin_count = min(coin_count,min_coins[cent - j] + 1)
        min_coins[cent] = coin_count
    return min_coins[change]
print(make_change([1 , 5 ,8 ,10 , 21 , 25 ], 33 , {}))
