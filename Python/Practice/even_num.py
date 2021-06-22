import math
import os
import random
import re
import sys

def even(start, n):
    even_num =[0] * n
    # write your code here
    i = 0
    k = start 
    while (i < n):
        even_num[i] = k
        k += 2
        i += 1
        
    return even_num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    start, n = map(int, raw_input().split())
    res = even(start, n)
    assert type(res) == list
    fptr.write(" ".join(map(str, res)) + '\n')
    fptr.close()