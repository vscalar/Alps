import sys
input = sys.stdin.readline
from collections import deque, defaultdict

#https://www.acmicpc.net/problem/32866

if __name__ == "__main__":
    #get N, K
    N, K = map(int, input().split())
    #make ans and queue
    ans = 0
    queue = deque()
    #record close friend's name length in default dict
    length_count = defaultdict(int)
    #get student names
    for _ in range(N):
        name = input().strip()
        length = len(name)
        #count close friends with same length and add to ans
        ans += length_count[length]
        
        if len(queue) == K:
            #get pop from queue and renew length_count
            removed_length = queue.popleft()
            length_count[removed_length] -= 1
            if length_count[removed_length] == 0:
                del length_count[removed_length]
        
        queue.append(length)
        length_count[length] += 1
        
    print(ans)