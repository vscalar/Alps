import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/15665

#make a seq and print
def dfs(stack:list[int], nums:list[int], M:int) -> None:
    nums.sort()
    if len(stack) == M:
        #print the stack
        print(' '.join(map(str, stack)))
        return
    #record used num
    record = []
    for i in range(len(nums)):
        num = nums[i]
        #remove duplicate numbers
        if num in record:
            continue
        #keep it non-descending
        if stack and stack[-1] > num:
            continue
        record.append(num)
        stack.append(num)
        dfs(stack, nums, M)
        #find other cases
        stack.pop()

if __name__ == "__main__":
    #get N, M
    N, M = map(int, input().split())
    #get sorted nums
    nums = list(map(int, input().split()))
    stack = []
    dfs(stack,nums,M)