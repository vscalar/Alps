import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/2580
def get_possible(coor, matrix):
    x, y = coor
    possible_set = set(range(1, 10))
    #check row
    possible_set = possible_set - set(matrix[x])
    #check column
    for i in range(9):
        num = matrix[i][y]
        possible_set.discard(num)
    #check box
    x_box, y_box = x//3,y//3
    for i in range(x_box*3, x_box*3+3):
        for j in range(y_box*3, y_box*3+3):
            num = matrix[i][j]
            possible_set.discard(num)
    return list(possible_set)

def backtracking(matrix):
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                have_zero = True
                possibles = get_possible((i,j), matrix)
                if not possibles:
                    return
                for num in possibles:
                    matrix[i][j] = num
                    backtracking(matrix)
                    matrix[i][j] = 0
                return
    for i in range(9):
        print(*matrix[i])
    exit()

if __name__ == "__main__":
    #get matrix
    matrix = list(list(map(int, input().split())) for _ in range(9))
    backtracking(matrix)
