#1
def make_change_1(face_value_list, change):
    if change in face_value_list:
        return 1
    min_value = float("inf")
    for i in[j for j in face_value_list if j <= change]:
        num_coins = 1 + make_change_1(face_value_list , change - i)
        min_value = min(min_value, num_coins)
    return min_value
print(make_change_1((1 , 5 , 10 , 25 ) , 63)) 

2(添加查询表)
import timeit
def make_change_2(face_value_list, change, known_results):
    min_coins = change
    if change in face_value_list:
        return 1
    elif change in known_results:
        return known_results[change]
    else:
        for i in [j for j in face_value_list if j <= change]:
            num_coins = 1 + make_change_2(face_value_list , change - i, known_results)
            min_coins = min(min_coins, num_coins)
        known_results[change] = min_coins
        return min_coins
print(make_change_2([1, 5, 10, 25] , 62 , {}))
print(timeit.timeit(lambda : make_change_2([1, 5, 10, 25] , 62 , {}) , number =  1))




def make_change_3(face_value_list, change, min_coins):
    for cents in range(change + 1):
        coin_count = cents
        for j in [c for c in face_value_list if c <= cents]:
            if min_coins[cents - j] + 1 <coin_count:
                coin_count = min_coins[cents - j] + 1
        min_coins[cents] = coin_count
    return min_coins[change]

print(make_change_3([1, 5, 10, 25] , 62 , {}))
print(timeit.timeit(lambda : make_change_3([1, 5, 10, 25] , 62 , {})))

import timeit
def make_change_4(coin_value_list, change, min_coins, coins_used):
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    return min_coins[change]

def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        print(coins_used[coin] , end = " ")
        coin = coin - coins_used[coin]
    print()

def main():
    amnt = 63
    coin_list = [1 , 5 , 10 , 21, 25]
    coins_used = {}
    coin_count = {}
    print(f"Making change for {amnt} ", end = " ")
    print(f"requiring the following {make_change_4( coin_list , amnt, coin_count, coins_used)} coins:")
    print_coins(coins_used, amnt)
    print("Thw used list is as follows:")
    print(coins_used, end = " ")
print(timeit.timeit(main, number= 100)) 





