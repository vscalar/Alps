import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lectures = list(map(int, input().split()))

def isEnoughLength(length: int, M: int, lectures: list[int]) -> bool:
    blurayCount = 1
    curLength = 0
    
    for lec in lectures:
        if lec > length:
            return False

        if curLength == 0:             #첫번째 인덱스
            curLength = lec
        
        elif curLength + lec > length: #다음 강의 넣으면 초과
            blurayCount += 1
            curLength = lec
        
        else:                          #다음 강의 넣어도 초과 안함
            curLength += lec
        
    return blurayCount <= M

#print(isEnoughLength(16, 3, lectures))

def findLength(low: int, high: int, M: int, ans: int, lectures: list[int]) -> int:
    if low > high:
        return ans
    
    mid = (low + high) // 2
    
    isEnough = isEnoughLength(mid, M, lectures)
    
    if isEnough:
        return findLength(low, mid-1, M, mid, lectures)
    
    else:
        return findLength(mid+1, high, M, ans, lectures)

minimum = sum(lectures) // M
maximum = sum(lectures)
print(findLength(minimum, maximum, M, 0, lectures))