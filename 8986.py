import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def getMoveDistance(interval: int, N:int, positions: list[int]) -> int:
    ans = 0
    for i in range(len(positions)):
        pos = positions[i]
        ans += abs(pos - i * interval)
    
    return ans

def getMinDistance(low: int, high:int, N:int, positions: list[int]) -> int:
    if high - low < 3:
        return min(getMoveDistance(low, N, positions), getMoveDistance(low+1,  N, positions), getMoveDistance(low+2,  N, positions))
    
    oneThird = (low * 2 + high) // 3
    twoThird = (low + high * 2) // 3
    
    if getMoveDistance(oneThird, N, positions) > getMoveDistance(twoThird, N, positions):
        return getMinDistance(oneThird, high, N, positions)

    else:
        return getMinDistance(low, twoThird, N, positions)
    
N = int(input())
positions = list(map(int, input().split()))

#print(getMoveDistance(1, N, positions))

print(getMinDistance(1, max(positions), N, positions))
