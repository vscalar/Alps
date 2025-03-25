import sys
input = sys.stdin.readline
from collections import deque

#https://www.acmicpc.net/problem/5430

if __name__ == "__main__":
    #get T
    T = int(input())
    for _ in range(T):
        #get instruction
        instr = input().strip()
        #get length of array 
        length = int(input())
        #get array
        string = input().strip()
        if len(string) == 2:
            deq = deque()
        else:
            deq = deque(map(int, string[1:-1].split(',')))
        #set is_reversed
        is_reversed = False

        for letter in instr:
            if letter == 'R':
                #change the state of is_reversed
                is_reversed = not is_reversed
            elif letter == 'D':
                #empty deq but called 'D'
                if not deq: 
                    deq = -1
                    break
                if is_reversed:
                    #pop from right
                    deq.pop()
                else:
                    #pop from left
                    deq.popleft()
        
        if deq == -1:
            print("error")
            continue

        print('[',end='')
        if is_reversed:
            #print reversed deq
            print(*reversed(deq),sep=',',end='')
        
        else:
            print(*deq,sep=',',end='')
        print(']',end='\n')