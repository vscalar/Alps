import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/9663

def is_N_queen(index):
    for i in range(index):
        #check if two queens are in the same row or diagonal
        if sequence[index] == sequence[i] or abs(sequence[index] - sequence[i]) == abs(index - i):
            return False
    
    return True

def Backtracking(depth, sequence):
    ans = 0
    if depth == n:
        return 1

    for i in range(n):
        sequence[depth] = i
        if is_N_queen(depth):
            ans += Backtracking(depth+1, sequence)
    return ans
            

if __name__ == "__main__":
    n = int(input())
    sequence = [0] * n
    
    ans = Backtracking(0, sequence)
    print(ans)