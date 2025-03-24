import sys
input = sys.stdin.readline
from collections import deque

#https://www.acmicpc.net/problem/11003

if __name__ == "__main__":
    #get N, L
    N, L = map(int, input().split())
    #get seq
    seq = list(map(int, input().split()))
    #set ans and queue
    ans = []
    queue = deque()

    for i in range(N):
        #pop until the new element is larger than the back of queue
        while queue and queue[-1][1] > seq[i]: 
            queue.pop()
        #if front of queue is outdated, popleft
        if queue and i - queue[0][0] == L:
            queue.popleft()
        #append (index, num)
        queue.append((i, seq[i]))
        ans.append(queue[0][1])
    
    print(*ans)