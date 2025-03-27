import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/15657

#make a seq and print
def dfs(stack:list[int], nums:list[int], N:int, M:int) -> None:
    nums.sort()
    if len(stack) == M:
        #print the stack
        print(' '.join(map(str, stack)))
        return
    
    for i in range(N):
        #ignore if top of stack is larger than num
        if stack and stack[-1] > nums[i]:
            continue
        stack.append(nums[i])
        dfs(stack, nums, N, M)
        #find other cases
        stack.pop()

if __name__ == "__main__":
    #get N, M
    N, M = map(int, input().split())
    #get sorted nums
    nums = list(map(int, input().split()))
    nums.sort()
    stack = []
    dfs(stack,nums, N,M)