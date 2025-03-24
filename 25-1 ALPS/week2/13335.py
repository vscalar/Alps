import sys
input = sys.stdin.readline
from collections import deque

def get_required_time(truck_num, w):
    return w+truck_num

#https://www.acmicpc.net/problem/13335

if __name__ == "__main__":
    #get n, w, L
    n, w, L = map(int, input().split())
    #get truck weight list
    truck_weights = list(map(int, input().split()))
    #set queue
    queue = deque([0]*w)
    #ans
    ans = 0

    for weight in truck_weights:
        #wait until weight on bridge lowers
        while sum(queue)- queue[0] + weight > L: 
            queue.popleft()
            queue.append(0)
            ans += 1
        #put another truck
        queue.popleft()
        queue.append(weight)                    
        ans += 1
    #move the last truck and print ans
    print(ans + w)