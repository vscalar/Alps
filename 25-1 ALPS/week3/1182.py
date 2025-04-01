import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/1182

#made this subseq and searched until index, find the number of subseq
def backtracking(subseq, index):
    ans = 0
    #if subseq has element and sum is S
    if len(subseq) and sum(subseq) == S:
        ans += 1
    #iterate
    for i in range(index+1, N):
        subseq.append(seq[i])
        ans += backtracking(subseq, i)
        subseq.pop()
    return ans

if __name__ == "__main__":
    #get N, S
    N, S = map(int, input().split())
    #get seq
    seq = list(map(int, input().split()))

    #print ans
    print(backtracking([], -1))