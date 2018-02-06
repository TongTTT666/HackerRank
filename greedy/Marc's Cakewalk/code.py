#!/bin/python3

import sys

def marcsCakewalk(calorie):
    # Complete this function
    # 直接由大到小排序就ok了
    calorie = sorted(calorie, reverse=True)
    sum = 0
    for i, val in enumerate(calorie):
        sum += 2**i * val
    return sum
  
if __name__ == "__main__":
    n = int(input().strip())
    calorie = list(map(int, input().strip().split(' ')))
    result = marcsCakewalk(calorie)
    print(result)

