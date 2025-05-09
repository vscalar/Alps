import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/11722

def get_length_of_decreasing_subsequence(length:int, sequence:list[int])->int:
    if length <= 0:
        return 0
    
    dp = [1] * length

    for i in range(1, length):
        max_len = 0
        for j in range(i):
            if sequence[i] < sequence[j]:
                max_len = max(max_len, dp[j])
        dp[i] += max_len
    return max(dp)

if __name__ == "__main__":
    n = int(input())
    sequence = list(map(int, input().split()))
    print(get_length_of_decreasing_subsequence(n, sequence))