import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/2630

# check if a sqare consists of a single color
def is_same_color(matrix, coor, size):
    x, y = coor
    color = matrix[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if color != matrix[i][j]:
                return False
    
    return True

def get_sqare_num(matrix, size, coor=(0,0)):
    white_square = 0
    blue_square = 0
    x, y = coor
    dx = [0, 1, 1, 0]
    dy = [0, 1, 0, 1]
    if is_same_color(matrix, coor, size):
        if matrix[x][y] == 1:
            blue_square += 1
        else:
            white_square += 1
    else:
        next_size = size//2
        for i in range(4):
            nx = x + dx[i] * next_size
            ny = y + dy[i] * next_size
            w, b = get_sqare_num(matrix, next_size, (nx,ny))
            white_square += w
            blue_square += b
    
    return white_square, blue_square

if __name__ == "__main__":
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    w, b = get_sqare_num(matrix, N)
    print(w)
    print(b)

