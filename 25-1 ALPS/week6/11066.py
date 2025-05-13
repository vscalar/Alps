import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/11066

def get_min_cost(n, seq):
    
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + seq[i]

    def range_sum(i, j):
        return prefix_sum[j + 1] - prefix_sum[i]

    dp = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]

    for length in range(2, n + 1):  # chain length
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + range_sum(i, j)
                dp[i][j] = min(dp[i][j], cost)

    print(dp[0][n-1])

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        seq = tuple(map(int, input().split()))
        get_min_cost(n, seq)
