import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/1463

def get_min_actions(n:int)->int:
    dp = [float('inf')]*(n+1)
    dp[n] = 0

    for i in range(n, 1, -1):
        dp[i-1] = min(dp[i-1], dp[i]+1)
        if i%3 == 0:
            dp[i//3] = min(dp[i//3], dp[i]+1)
        if i%2 == 0:
            dp[i//2] = min(dp[i//2], dp[i]+1)
    
    return dp[1]

if __name__ == "__main__":
    n = int(input())
    print(get_min_actions(n))
