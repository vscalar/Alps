import sys
import math
input = sys.stdin.readline

def getDistance(pos1: list[int], pos2: list[int]) -> float:
    return math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)



