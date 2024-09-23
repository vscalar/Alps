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

ans = 0
def findLength(low: int, high: int, lines: list[int]) -> int:
    if low > high:
        return
    
    global ans
    mid = (low + high) // 2
    
    isSolvable = isSolved(mid, lines, N)
    
    if isSolvable:
        ans = mid
        findLength(mid+1, high, lines)
    
    else:
        findLength(low, mid-1, lines)

findLength(1, max(lines), lines)
print(ans)