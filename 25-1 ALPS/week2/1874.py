import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/32864

if __name__ == "__main__":
    #make a stack
    stack = []

    #get N
    N = int(input())

    #ans
    ans = []

    seq = [int(input()) for _ in range(N)]
    cur_num = 1

    for seq_num in seq:
        for _ in range(cur_num, seq_num+1):
            stack.append(cur_num)
            cur_num += 1
            ans.append("+")
        
        if stack[-1] == seq_num:
            ans.append("-")
            stack.pop()
        
        else:
            print("NO")
            exit()
    
    for symbol in ans:
        print(symbol)