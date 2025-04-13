import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/1074

def get_pos(N, r, c):
    if N == 0:
        return 0
    pos = 0
    nr = r
    nc = c
    criterion = pow(2, N-1)

    if r >= criterion:
        pos += 2
        nr -= criterion
    if c >= criterion:
        pos += 1
        nc -= criterion
    
    return pos * pow(criterion,2) + get_pos(N-1, nr, nc)
    
    
if __name__ == "__main__":
    N, r, c = map(int, input().split())
    print(get_pos(N,r,c))
