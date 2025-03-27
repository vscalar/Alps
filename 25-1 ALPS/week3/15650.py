import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/15650
#make a seq and print
def dfs(stack:list, N:int, M:int) -> None:
    if len(stack) == M:
        #print the stack
        print(' '.join(map(str, stack)))
        return
    
    for i in range(1, N+1):
        if i not in stack and (not stack or stack[-1] < i):
            #add a num not in stack
            stack.append(i)
            #pick rest of the nums
            dfs(stack, N, M)
            #find other cases
            stack.pop()

if __name__ == "__main__":
    #get N, M
    N, M = map(int, input().split())
    stack = []
    dfs(stack,N,M)