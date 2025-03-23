import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/32384

sentence = "LoveisKoreaUniversity"

if __name__ == "__main__":
    #get N
    N = int(input())
    
    #print sentence for N times
    for _ in range(N):
        print(sentence, end=" ")