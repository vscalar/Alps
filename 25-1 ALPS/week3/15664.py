import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/15664

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
        #keep it non-descending
        if stack and stack[-1] > num:
            continue
        #remove duplicate numbers
        if num in record:
            continue
        record.append(num)
        stack.append(num)
        #make a list that num is deleted
        new_nums = nums[:i] + nums[i+1:]
        dfs(stack, new_nums, M)
        #find other cases
        stack.pop()

if __name__ == "__main__":
    #get N, M
    N, M = map(int, input().split())
    #get sorted nums
    nums = list(map(int, input().split()))
    nums.sort()
    stack = []
    dfs(stack,nums,M)