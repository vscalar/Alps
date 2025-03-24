import sys
input = sys.stdin.readline
from collections import deque

#https://www.acmicpc.net/problem/1158

#rotate n times
def rotate(queue: deque, n: int) -> deque:
    if not queue:
        raise ValueError
    for _ in range(n):
        front = queue.popleft()
        queue.append(front)
    return queue

if __name__ == "__main__":
    #get N, K
    N, K = map(int, input().split())
    #initialize queue
    queue = deque(range(1,N+1))
    #set ans
    ans = []

    for _ in range(N):
        #rotate K-1 times and popleft
        queue = rotate(queue, K-1)
        ans.append(queue.popleft())
    
    print('<', end='')
    print(*ans,sep=', ',end='')
    print('>')


