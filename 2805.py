import sys
input = sys.stdin.readline

def isEnoughChoppedWood(H: int, M:int, trees: list[int]) -> bool:
    wood = 0
    for tree in trees:
        if tree > H:
            wood += tree - H
        
        else:
            pass
    
    return wood >= M

N, M = map(int, input().split())
trees = list(map(int, input().split()))

def findH(low: int, high: int, M: int, ans: int, trees: list[int]) -> int:
    if low > high:
        return ans
    
    mid = (low + high) // 2
    
    isEnough = isEnoughChoppedWood(mid, M, trees)
    
    if isEnough:
        return findH(mid+1, high, M, mid, trees)
    
    else:
        return findH(low, mid-1, M, ans, trees)

print(findH(1, max(trees), M, 0, trees))

