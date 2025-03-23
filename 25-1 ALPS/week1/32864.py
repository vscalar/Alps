import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/32864

if __name__ == "__main__":
    #winner list
    winners = ["mnx","alsdkffhgk"]
    winner = -1 #-1: mnx, 1: alsdkffhgk

    #get N
    N = int(input())
    #get stations
    stations = list(map(int, input().split()))
    

    for i in range(1, N):
        if stations[i] == 1: #if transfer right ahead
            winner *= -1 #winner changes
        
        else:
            break
    
    #print winner
    if winner == -1:
        print(winners[0])
    else:
        print(winners[1])


