# 문제: https://www.acmicpc.net/problem/2577

A = int(input())
B = int(input())
C = int(input())
multi = A * B * C

for i in range(10): # A x B x C 의 결과에 0부터 9까지의 숫자가 각각 몇 번 쓰였는지 count
    count = 0
    for j in range(len(str(multi))):
        if int(str(multi)[j]) == i:
            count += 1
    print(count)
