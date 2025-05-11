import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/11049

def main():
    N = int(input())
    matrices = [tuple(map(int, input().split())) for _ in range(N)]
    
    dp = [[0 if i == j else float('inf') for j in range(N)] for i in range(N)]

    for length in range(2, N + 1):  # chain length
        for i in range(N - length + 1):
            j = i + length - 1
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]
                dp[i][j] = min(dp[i][j], cost)

    print(dp[0][N-1])

if __name__ == "__main__":
    main()
