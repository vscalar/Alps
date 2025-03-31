import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/14500

#shapes of tetromino
dx = ((1,2,3), (0,0,0), (0,1,1), (0,0,-1), (0,0,-1), (0,0,1), (0,0,1), (-1,-2,-2), (-1,-2,-2), (1,2,2), (1,2,2), (1,1,2), (1,1,2), (0,1,1), (0,1,1), (1,1,2), (0,0,1), (1,1,2), (1,1,1))
dy = ((0,0,0), (1,2,3), (1,1,0), (-1,-2,-2), (1,2,2), (-1,-2,-2), (1,2,2), (0,0,-1), (0,0,1), (0,0,-1), (0,0,1), (0,-1,-1),(0,1,1), (-1,-1,-2), (1,1,2), (0,1,0), (1,2,1), (0,-1,0), (-1,0,1))
tet_num = len(dx)

def get_largest_sum_tetromino(map:list[list[int]], coor,N:int,M:int) -> int:
    x, y = coor
    ret = 0
    #iterate through tetrominos
    for i in range(tet_num):
        tmp = 0
        for j in range(3):
            nx = x + dx[i][j]
            ny = y + dy[i][j]
            #if in range add its value
            if 0 <= nx < N and 0<= ny < M:
                tmp += map[nx][ny]
            #if not in range make tmp 0
            else:
                tmp = 0
                break
        ret = max(ret, tmp)
    #add value from (x, y)
    return ret + map[x][y]


if __name__ == "__main__":
    #get N,M
    N, M = map(int, input().split())
    #get map
    map = [list(map(int, input().split())) for _ in range(N)]
    #print(tetromino(map))
    #set ans
    ans = 0
    #iterate through map
    for x in range(N):
        for y in range(M):
            ans = max(ans, get_largest_sum_tetromino(map, (x,y), N, M))
    
    print(ans)