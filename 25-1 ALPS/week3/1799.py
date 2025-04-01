import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

#https://www.acmicpc.net/problem/1799

def backtracking(index, N, diagonal_l, diagonal_r, positions):
    if index == len(positions):
        return 0

    x, y = positions[index]
    #index of left to right diagonal(just make it larger than 0)
    d1 = x-y + N - 1
    #index of right to left diagonal
    d2 = x+y 

    ans = backtracking(index+1, N, diagonal_l, diagonal_r, positions)
    #if both d1 and d2 are not visited in diagonal's pov
    if not diagonal_l[d1] and not diagonal_r[d2]:
        diagonal_l[d1] = diagonal_r[d2] = True
        ans = max(ans, 1+backtracking(index+1, N, diagonal_l, diagonal_r, positions))
        diagonal_l[d1] = diagonal_r[d2] = False
    #if visited, just move on to next position
    
    return ans

def get_max_bishop(matrix, N):
    black, white = [], []
    for x in range(N):
        for y in range(N):
            if matrix[x][y] == 1:
                if (x+y) % 2 == 0:
                    black.append((x,y))
                else:
                    white.append((x,y))
    dl_black = [False] * (2 * N)
    dr_black = [False] * (2 * N)
    dl_white = [False] * (2 * N)
    dr_white = [False] * (2 * N)
    #get num of bishop from both black and white
    return backtracking(0, N, dl_black, dr_black, black) + backtracking(0, N, dl_white, dr_white, white)


if __name__ == "__main__":
    #get N
    N = int(input())
    #get matrix
    matrix = list(list(map(int, input().split())) for _ in range(N))
    #get ans
    print(get_max_bishop(matrix, N))