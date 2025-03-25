import sys
input = sys.stdin.readline
from collections import deque

#https://www.acmicpc.net/problem/10866

def pop_front(deq):
    if len(deq) > 0:
        print(deq.popleft())
    else:
        print(-1)
def pop_back(deq):
    if len(deq) > 0:
        print(deq.pop())
    else:
        print(-1)

def empty(deq):
    if len(deq) == 0:
        print(1)
    else:
        print(0)

def front(deq):
    if len(deq) > 0:
        print(deq[0])
    else:
        print(-1)

def back(deq):
    if len(deq) > 0:
        print(deq[-1])
    else:
        print(-1)

if __name__ == "__main__":
    #get N
    N = int(input())
    #make a queue
    deq = deque()

    #get instructions, proccess
    for _ in range(N):
        instr = input().split()
        #print(instr)
        if len(instr) == 2 and instr[0] == "push_front":
            num = int(instr[1])
            deq.appendleft(num)
            continue
        elif len(instr) == 2 and instr[0] == "push_back":
            num = int(instr[1])
            deq.append(num)
            continue
        
        if instr[0] == "pop_front":
            pop_front(deq)
        
        elif instr[0] == "pop_back":
            pop_back(deq)
        
        elif instr[0] == "size":
            print(len(deq))
        
        elif instr[0] == "empty":
            empty(deq)
        
        elif instr[0] == "front":
            front(deq)
        
        elif instr[0] == "back":
            back(deq)
        
        else:
            raise NameError