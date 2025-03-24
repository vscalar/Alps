import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/2493

if __name__ == "__main__":
    #get N
    N = int(input())
    #get tower list
    tower_list = list(map(int, input().split()))
    #make stack and ans
    stack = []
    ans = []

    for i in range(N):
        while stack:
            if stack[-1][1] > tower_list[i]:    #if height of closest tower is higher
                ans.append(stack[-1][0] + 1)    #record num of closest tower and don't append
                break
            else:
                stack.pop()                     #remove a tower from stack
        if not stack:
            ans.append(0)                       #no tower on the left thus 0
        stack.append((i, tower_list[i]))        #append (num of tower, height of tower)
    print(*ans, sep=' ')