import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/32385

if __name__ == "__main__":
    #get N
    N = int(input())
    
    sequence = []
    
    #where N is even
    if N % 2 == 0:
        
        #make a even length sequence with sum 0
        for i in range(1, N//2 + 1):
            sequence.append(i)
            sequence.append(-i)
        
        #end with 0
        sequence.append(0)
    
    #where N is odd
    else:
        #make a odd length sequence with sum N
        sequence.append(N)
        for i in range(1, N//2 + 1):
            sequence.append(N + i)
            sequence.append(-N - i)
        
        #end with 1
        sequence.append(1)
    
    #print the sequence
    print(" ".join(map(str, sequence)))