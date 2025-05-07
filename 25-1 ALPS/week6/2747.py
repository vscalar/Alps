import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/2747

#get n
n = int(input())

#initialize fibo_list
fibo_list = [0, 1]

#calculate fibo_list
for i in range(2, n+1):
    next = fibo_list[i-1] + fibo_list[i-2]
    fibo_list.append(next)

print(fibo_list[n])

