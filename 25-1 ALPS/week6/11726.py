import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/11726

MOD = 10007
# get n
n = int(input())

dp = [0, 1, 2]

# generate dp until n
while len(dp) <= n:
    next_val = (dp[-1] + dp[-2])%MOD
    dp.append(next_val)

print(dp[n])