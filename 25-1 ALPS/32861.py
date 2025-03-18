import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/32861

def is_diagonal_0(matrix, N):
    for i in range(N):
        if matrix[i][i] != 0:
            return False
    
    return True

def get_sequence(matrix, N):
    res = []
    for row in matrix:
        count_1 = row.count(1)
        num = N - count_1
        res.append(num)

    return res

def has_duplicates(sequence):
    return len(sequence) != len(set(sequence))

def get_triangle_num(num):
    return (num + 1) * num // 2

if __name__ == "__main__":
    #get N and matrix
    N = int(input())
    matrix = list(list(map(int, input().split())) for _ in range(N))

    #check diagonal
    if not is_diagonal_0(matrix, N):
        print(-1)
        exit()

    #check made sequence
    sequence = get_sequence(matrix, N)
    sumation = sum(sequence)
    N_triangle_num = get_triangle_num(N)
    if sumation != N_triangle_num:
        print(-1)
        exit()

    if has_duplicates(sequence):
        print(-1)
        exit()
    
    print(*sequence)
    
    
