import sys
input = sys.stdin.readline

def get2SumList(sequence: list[int]) -> list[int]:
    ans = list()
    for i in range(len(sequence)):
        for j in range(i, len(sequence)):
            ans.append(sequence[i] + sequence[j])
    
    ans.sort()
    return set(ans)

length = int(input())
sequence = list()

for _ in range(length):
    num = int(input())
    sequence.append(num)
    
sequence.sort()
sumSequence = get2SumList(sequence)
#print(sumSequence)

def solve(sequence, sumSequence) -> int:
    for i in range(length-1,-1,-1):
        for j in range(i):
            if sequence[i] - sequence[j] in sumSequence:
                return sequence[i]

print(solve(sequence, sumSequence))