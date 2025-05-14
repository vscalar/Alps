import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/11047

def get_min_coin(price: int, coins: list[int]) -> int:
    # sort coins in descending order
    coins_sorted = sorted(coins, key=lambda x : -x)
    # initialize ans and cur_price
    ans = 0
    cur_price = price
    for i in range(len(coins_sorted)):
        # break if the coins summed up to the price
        if cur_price == 0:
            break
        coin = coins_sorted[i]
        ans += cur_price // coin
        cur_price %= coin

    return ans

def main():
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    print(get_min_coin(k, coins))

if __name__ == "__main__":
    main()