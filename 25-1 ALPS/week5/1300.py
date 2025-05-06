import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/1300

if __name__ == "__main__":
    #get N
    N = int(input())
    #get K
    K = int(input())
    #set start and end
    start = 1
    end = pow(N, 2)

    while start <= end:
        mid = (start + end) // 2
        #print(f'{mid = }')
        behind = 0
        # get the number of those who are behind mid
        for i in range(1, N+1):
            behind += min(N,mid // i)
        #print(f'{behind = }')
        if behind >= K:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    print(result)