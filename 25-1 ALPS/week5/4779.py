import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/4779

def cantor(N):
    if N == 1:
        return '-'
    divided_length = N//3
    empty = ' ' * (divided_length)
    next = cantor(divided_length)
    return next + empty + next

if __name__ == "__main__":
    while True:
        try:
            N = int(input())
            length = pow(3, N)
            print(cantor(length))
        except:
            break