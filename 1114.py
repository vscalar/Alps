import sys
input = sys.stdin.readline

def findCutIndex(length: int, L: int, K: int, C: int, cutPos: list[int]) -> int:
    pass
        
def findLength(low: int, high: int, L: int, C: int, ans: int, cutPos: list[int]) -> int:
    if low > high:
        return ans
    
    mid = (low + high) // 2
    isEnough = findCutIndex(mid, L, K, C, cutPos)
    
    if isEnough != -1:
        return findLength(low, mid-1, L, C, mid, cutPos)

    else:
        return findLength(mid+1, high, L, C, ans, cutPos)
    
L, K, C = map(int, input().split())
cutPos = list(map(int, input().split()))

cutPos.sort()

#print(findFirstCut(4, L, C, cutPos))

length = findLength(1, L, L, C, 0, cutPos)
cutIndex = findCutIndex(length, L, K, C, cutPos)

print(length, cutPos[cutIndex])
    