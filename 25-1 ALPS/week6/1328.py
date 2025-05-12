import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/1328

MOD = 1000000007

if __name__ == "__main__":
    n, left, right = map(int, input().split())

    dp = [[[0]*(n+1) for _ in range(n+1)] for _ in range(n+1)]
    dp[1][1][1] = 1
    
    # placing buildings from taller ones
    for i in range(2, n+1):
        for j in range(1, left+1):
            for k in range(1, right+1):
                # building placed between others, left side, right side
                dp[i][j][k] = (dp[i-1][j][k] * (i-2) + dp[i-1][j-1][k] + dp[i-1][j][k-1]) % MOD
               
    print(dp[n][left][right])