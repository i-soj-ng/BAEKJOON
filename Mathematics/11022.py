# 문제: https://www.acmicpc.net/problem/15552

import sys
t = int(input())

for i in range(t):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)