import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/31831

if __name__ == "__main__":
    #get N, M, stress_list
    N, M = map(int, input().split())
    stress_list = list(map(int, input().split()))
    
    #answer
    ans = 0
    
    #current stress amount
    stress = 0
    
    #count days
    for day in range(N):
        stress = max(0, stress + stress_list[day])
        if stress >= M:
            ans += 1
    
    #print answer
    print(ans)
    