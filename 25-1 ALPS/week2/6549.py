import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/6549

"""
#calculates area of largest rectangle
def get_largest_rectangle(seq):
    stack = []
    ans = 0
    seq.append(0)

    for i in range(len(seq)):
        #remove column that is higher than current one and calculate area
        while stack and seq[stack[-1]] > seq[i]:
            index = stack.pop()
            height = seq[index]
            #if empty stack, start ~ i else i ~ column
            width = i if not stack else i - stack[-1] - 1
            ans = max(ans, height * width)
        stack.append(i)
    
    #print(stack)
    #process the remains
    while stack:
        index = stack.pop()
        height = seq[index]
        #if empty stack, start ~ len(seq) else len(seq) ~ next column
        width = len(seq) if not stack else len(seq) - stack[-1] - 1
        ans = max(ans, height * width)

    return ans
"""

def largestRectangleArea(heights):
    stack = []  # stack to store indices of the histogram bars
    max_area = 0  # variable to keep track of the maximum area
    heights.append(0)  # Append a zero at the end to ensure all bars are processed

    for i in range(len(heights)):
        # Pop from stack while the current bar is shorter than the bar at stack's top
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]  # height of the bar
            w = i if not stack else i - stack[-1] - 1  # width of the rectangle
            max_area = max(max_area, h * w)  # update the max_area

        stack.append(i)  # push current bar's index to stack

    return max_area

if __name__ == "__main__":
    while True:
        seq = list(map(int, input().split()))
        if seq == [0]:
            break
        
        print(largestRectangleArea(seq))