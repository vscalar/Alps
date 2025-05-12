import sys
import bisect
input = sys.stdin.readline

#https://www.acmicpc.net/problem/14003

def main():
    length = int(input())
    sequence = list(map(int, input().split()))
    
    dp = []  
    pos = [0] * length  

    for i in range(length):
        num = sequence[i]
        # gets position for num in dp
        idx = bisect.bisect_left(dp, num)
        # num is bigger than any element in dp
        if idx == len(dp):
            dp.append(num)
        # put num inside dp
        else:
            dp[idx] = num
        
        # record position of num in dp
        pos[i] = idx

    # Reconstruct the subseq
    subseq_length = len(dp)
    answer = []
    current_len = subseq_length - 1
    for i in range(length - 1, -1, -1):
        # find head of subseq
        if pos[i] == current_len:
            answer.append(sequence[i])
            current_len -= 1
        if current_len < 0:
            break

    print(subseq_length)
    print(*reversed(answer))

if __name__ == "__main__":
    main()