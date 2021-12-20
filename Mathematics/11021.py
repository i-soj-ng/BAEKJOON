# 문제: https://www.acmicpc.net/problem/11021

T = int(input())
test_cases = [list(map(int, input().split())) for j in range(T)]

for i in range(len(test_cases)):
    print("Case #{}:" .format(i+1), test_cases[i][0] + test_cases[i][1])
