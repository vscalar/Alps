import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/9095

#get testcase num
t = int(input())

dp = [0, 1, 2, 4]
for _ in range(t):
    n = int(input())
    length = len(dp) 
    while length <= n:
        next_val = dp[-3] + dp[-2] + dp[-1]
        dp.append(next_val)
        length += 1
    
    print(dp[n])

