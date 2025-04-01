import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/1018
def get_min_change(coor, map):
    white_start = 0
    black_start = 0
    white_chess = ['WBWBWBWB', 'BWBWBWBW'] * 4
    black_chess = ['BWBWBWBW', 'WBWBWBWB'] * 4
    i, j = coor
    if i+8>N or j+8>M:
        return float('inf')
    
    for x in range(i, i+8):
        for y in range(j, j+8):
            if white_chess[x-i][y-j] != map[x][y]:
                white_start += 1
            if black_chess[x-i][y-j] != map[x][y]:
                black_start += 1
    return min(black_start,white_start)
    
if __name__ == "__main__":
    #get N, M
    N, M = map(int, input().split())
    #get map
    map = [input() for _ in range(N)]
    #set ans
    ans = float('inf')
    #iterate
    for x in range(N):
        for y in range(M):
            coor = (x, y)
            ans = min(ans, get_min_change(coor, map))
    
    print(ans)
