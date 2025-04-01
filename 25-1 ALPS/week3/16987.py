import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/16987

def backtracking(eggs, index, N):
    ans = 0
    #no eggs left
    if index == N:
        #count broken eggs
        for i in range(N):
            if eggs[i][0] <= 0:
                ans += 1
        return ans
    #broken egg
    if eggs[index][0] <= 0:
        #just grab next egg
        ans = max(ans, backtracking(eggs, index+1, N))
        return ans
    #break i-th egg
    for i in range(N):
        #don't break itself or broken egg
        if i == index or eggs[i][0] <= 0:
            continue
        #break egg
        eggs[index][0] -= eggs[i][1]
        eggs[i][0] -= eggs[index][1]
        ans = max(ans, backtracking(eggs, index+1, N))
        #backtrack
        eggs[index][0] += eggs[i][1]
        eggs[i][0] += eggs[index][1]
    #move to base case
    if ans == 0:
        ans = backtracking(eggs, N, N)
    return ans

if __name__ == "__main__":
    #get N
    N = int(input())
    #get eggs
    eggs = []
    for _ in range(N):
        egg = list(map(int, input().split()))
        eggs.append(egg)
    
    print(backtracking(eggs, 0, N))