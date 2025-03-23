import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/9012

if __name__ == "__main__":
    
    #get N
    N = int(input())

    for _ in range(N):
        
        #make a stack
        stack = []

        #get input
        ps = input().strip()
        #check vps
        is_vps = True 

        for p in ps:
            #not vps
            if not is_vps:          
                break

            if p == "(":
                stack.append("(")
            #rp occured when there's no lp
            elif len(stack) == 0:
                is_vps = False
                continue

            else:
                stack.pop()
        #used every string
        if is_vps and len(stack) == 0:
            print("YES")
        else:
            print("NO")