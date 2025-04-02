import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

#https://www.acmicpc.net/problem/13241
def gcd(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    while(num2):
        tmp = num1 % num2
        num1 = num2
        num2 = tmp
    return num1
    
if __name__ == "__main__":
    #get A, B
    A, B = map(int, input().split())
    #get gcd
    num = gcd(A,B)
    #print ans(num*a, num*)
    print(A*B//num)
