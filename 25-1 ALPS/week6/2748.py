import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/2748

# get n
n = int(input())

fibo = [0, 1]

# generate fibo until n
while len(fibo) <= n:
    next_val = fibo[-1] + fibo[-2]
    fibo.append(next_val)

print(fibo[n])
