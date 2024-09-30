def findParent(u):
    if parent[u] == u:
        return u

    parent[u] = findParent(parent[u])
    return parent[u]

def unionNode(u, v):
    u = findParent(u)
    v = findParent(v)
    if u != v: #if same node, then don't update
        parent[u] = v
        num[v] += num[u]
        num[u] = 0

R, C = map(int, input().split())
parent = [i for i in range(R*C)]
num = [1 for _ in range(R*C)]
chessBoard = [list(map(int, input().split())) for _ in range(R)]

def FindNearMin(x: int, y: int) -> tuple:
    dx, dy = [0, 0, 1, 1, 1, -1, -1, -1], [1, -1, 1, 0, -1, 1, -1, 0]
    curValue = chessBoard[x][y]
    minValue = 1e9
    minIndex = tuple()
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<R and 0<=ny<C:
            if chessBoard[nx][ny] < minValue:
                minValue = chessBoard[nx][ny]
                minIndex = (nx, ny)
    
    if minValue < curValue:
        return minIndex

    else:
        return (x, y)
    
def UnionBoard():
    for x in range(R): 
        for y in range(C):
            nearX, nearY = FindNearMin(x,y)
            curIndex = x*C + y
            nearIndex = nearX*C + nearY
            curValue = chessBoard[x][y]
            nearValue = chessBoard[nearX][nearY]
            if curValue > nearValue:
                unionNode(curIndex, nearIndex)
            else:
                pass

UnionBoard()
for i in range(R):
    print(*num[C*i:C*(i+1)])
