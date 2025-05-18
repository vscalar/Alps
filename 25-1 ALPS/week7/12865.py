import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/12865

def get_max_value(items: list[tuple[int, int]], weight_limit: int, item_count:int) -> int:
    dp = [[0]*(weight_limit+1) for _ in range(item_count+1)]
    for i in range(1, item_count+1):
        for j in range(1, weight_limit+1):
            weight = items[i][0]
            value = items[i][1]
            
            # could not take the item
            if j < weight:
                dp[i][j] = dp[i-1][j]
            # could take the item
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
                
    return dp[-1][-1]

def main():
    n, k = map(int, input().split())
    items = [(0,0)]+[tuple(map(int, input().split())) for _ in range(n)]
    ans = get_max_value(items, k, n)
    print(ans)
    

if __name__ == "__main__":
    main()