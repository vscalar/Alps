import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/2579

def get_max_score():
    # get n
    n = int(input())

    # get scores
    scores = [0] + [int(input()) for _ in range(n)]

    # set dp
    dp = [0] * (n+1)

    if n<=2:
        return sum(scores)

    dp[1] = scores[1]
    dp[2] = scores[1] + scores[2]

    for i in range(3, n+1):
        dp[i] = scores[i] + max(dp[i-2], scores[i-1]+dp[i-3])
    
    return dp[n]

print(get_max_score())
    