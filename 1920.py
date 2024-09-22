import sys
input = sys.stdin.readline

def contain_N(n: int, sequence: list) -> None:
    l = 0
    r = len(sequence)-1
    while l <= r:
        mid = (l + r) // 2
        if n == sequence[mid]:
            print(1)
            return
        
        elif n > sequence[mid]:
            l = mid + 1
        
        else:
            r = mid - 1
        
    print(0)

length = int(input())
sequence = list(map(int, input().split()))
sequence.sort()
num_of_N = int(input())
list_of_N = list(map(int, input().split()))

for N in list_of_N:
    contain_N(N, sequence)