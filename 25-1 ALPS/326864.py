import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/32864

def pop(stack):
    if len(stack) > 0:
        print(stack.pop())
    else:
        print(-1)

def top(stack):
    if len(stack) > 0:
        print(stack[-1])
    else:
        print(-1)

def empty(stack):
    if len(stack) == 0:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    #make a stack
    stack = []

    #get N
    N = int(input())

    #get instructions, proccess
    for _ in range(N):
        instr = input().split()
        #print(instr)
        if len(instr) == 2:
            num = int(instr[1])
            stack.append(num)
            continue
        
        if instr[0] == "top":
            top(stack)
        
        elif instr[0] == "size":
            print(len(stack))
        
        elif instr[0] == "empty":
            empty(stack)
        
        elif instr[0] == "pop":
            pop(stack)
        
        else:
            raise NameError