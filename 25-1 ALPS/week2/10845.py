import sys
input = sys.stdin.readline
import queue

#https://www.acmicpc.net/problem/32864

def pop(queue):
    if len(queue) > 0:
        print(queue.pop(0))
    else:
        print(-1)
def empty(queue):
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front(queue):
    if len(queue) > 0:
        print(queue[0])
    else:
        print(-1)

def back(queue):
    if len(queue) > 0:
        print(queue[-1])
    else:
        print(-1)

if __name__ == "__main__":
    #get N
    N = int(input())
    #make a queue
    queue = []

    #get instructions, proccess
    for _ in range(N):
        instr = input().split()
        #print(instr)
        if len(instr) == 2:
            num = int(instr[1])
            queue.append(num)
            continue
        
        if instr[0] == "pop":
            pop(queue)
        
        elif instr[0] == "size":
            print(len(queue))
        
        elif instr[0] == "empty":
            empty(queue)
        
        elif instr[0] == "front":
            front(queue)
        
        elif instr[0] == "back":
            back(queue)
        
        else:
            raise NameError