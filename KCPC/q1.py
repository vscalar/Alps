import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    sequence = []
    if N % 2 == 0:
        for i in range(1, N//2 + 1):
            sequence.append(i)
            sequence.append(-i)
        
        sequence.append(0)
    
    else:
        sequence.append(N)
        for i in range(1, N//2 + 1):
            sequence.append(N + i)
            sequence.append(-N - i)
        
        sequence.append(1)
    
    print(" ".join(map(str, sequence)))
    