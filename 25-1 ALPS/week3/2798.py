import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/2798

if __name__ == "__main__":
    #get N, M
    N, M = map(int, input().split())
    #get cards
    cards = list(map(int, input().split()))
    #set ans
    ans = 0
    #get 3 nums
    for i in range(N):
        for j in range(N):
            if j == i:
                continue
            for k in range(N):
                if k==i or k==j:
                    continue
                sum = cards[i] + cards[j] + cards[k]
                if sum > ans and sum <=M:
                    ans = sum
    #print ans
    print(ans)

                    