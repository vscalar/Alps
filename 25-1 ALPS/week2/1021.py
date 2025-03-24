import sys
input = sys.stdin.readline
from collections import deque

#https://www.acmicpc.net/problem/1021

if __name__ == "__main__":
    #get N, M
    N, M = map(int, input().split())
    #get nums
    nums = list(map(int, input().split()))
    #set ans
    ans= 0
    queue = deque(range(1,N+1))
    #iterate through nums
    for num in nums:
        while True:
            #do op1
            if queue[0] == num:
                queue.popleft()
                break
            #do op2 
            elif queue.index(num) <= len(queue)//2: 
                front = queue.popleft()
                queue.append(front)
                ans += 1
            #do op3
            else:
                back = queue.pop()
                queue.appendleft(back)
                ans += 1
    print(ans)
