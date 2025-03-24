import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/2504

if __name__ == "__main__":
    #get input
    ps = input().strip()
    #make a stack
    stack = []
    #ans
    ans = 0
    coefficient = 1
    for i in range(len(ps)):
        if ps[i] =='(':
            stack.append(ps[i])
            coefficient *= 2 #() scores 2
        elif ps[i] == '[':
            stack.append(ps[i])
            coefficient *= 3 #[] scores 3
        elif ps[i] == ")":
            if not stack or stack[-1] == "[": #mismatch
                ans = 0 
                break
            if ps[i-1] == "(":  #add ans only if previous letter matches
                ans += coefficient
            stack.pop()
            coefficient //= 2 #reset coefficient
        else:
            if not stack or stack[-1] == "(":
                ans=0
                break
            if ps[i-1] =='[':
                ans+=coefficient
            stack.pop()
            coefficient //=3
    if stack:
        print(0)
    else:
        print(ans)