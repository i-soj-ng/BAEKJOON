# 문제: https://www.acmicpc.net/problem/10952

test_cases = []
while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0: # '0 0'이 입력될 경우 입력 반복문 종료
        break

    test_cases.append([A, B])

for i in test_cases: # A+B 출력
    print(i[0] + i[1])
