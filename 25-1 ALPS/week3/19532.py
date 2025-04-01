import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/19532

if __name__ == "__main__":
    #get a~f
    a,b,c,d,e,f = map(int, input().split())
    #calculate x, y
    x = (-e*c + b*f) // (-e*a + d*b)
    y = (-d*c + a*f) // (-b*d + a*e)
    print(x, y)