import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/32866

if __name__ == "__main__":
    #get X
    o = int(input())
    X = int(input())
    #calculate ans
    ans = 100*X / (100 - X)
    #print ans
    print(ans)
