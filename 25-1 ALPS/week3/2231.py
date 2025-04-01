import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/2231

def is_inducer(x, target):
    string = str(x)
    #set digit_sum
    digit_sum = 0
    #sum up digits
    for digit in string:
        digit_sum += int(digit)
    #check if x is inducer of target
    if x + digit_sum == target:
        return True
    else:
        return False

if __name__ == "__main__":
    #get N
    N = int(input())
    #set ans
    ans = 0
    #iterate
    for i in range(N-1, N//2 - 1, -1):
        if is_inducer(i, N):
            ans = i
    print(ans)

