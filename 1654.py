import sys
input = sys.stdin.readline

def isSolved(length: int, lines: list[int], N: int) -> bool:
    ans = 0
    for line in lines:
        ans += line // length
    
    return ans >= N

K, N = map(int, input().split())
lines = list()

for _ in range(K):
    length = int(input())
    lines.append(length)


def findLength(low: int, high: int, ans: int, lines: list[int]) -> int:
    if low > high:
        return ans
    
    mid = (low + high) // 2
    
    isSolvable = isSolved(mid, lines, N)
    
    if isSolvable:
        return findLength(mid+1, high, mid, lines)
    
    else:
        return findLength(low, mid-1, ans, lines)

print(findLength(1, max(lines), 0, lines))