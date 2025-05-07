import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/1149

def get_cost_of_pos(matrix, position:tuple[int, int]):
    x, y = position
    if x+1 >= len(matrix):
        dp[x][y] = matrix[x][y]
        return dp[x][y]

    if dp[x][y] != 0:
        return dp[x][y]
    if y == 0:
        dp[x][y] = matrix[x][y] + min(get_cost_of_pos(matrix, (x+1, 1)), get_cost_of_pos(matrix, (x+1, 2)))
    elif y == 1:
        dp[x][y] = matrix[x][y] + min(get_cost_of_pos(matrix, (x+1, 0)), get_cost_of_pos(matrix, (x+1, 2)))
    else:
        dp[x][y] = matrix[x][y] + min(get_cost_of_pos(matrix, (x+1, 1)), get_cost_of_pos(matrix, (x+1, 0)))
        
    return dp[x][y]
N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]
for x in range(N-1, -1, -1):
    for y in range(3):
        get_cost_of_pos(matrix, (x, y))


print(min(dp[0]))
