# 문제: https://www.acmicpc.net/problem/4344

c = int(input())

for i in range(c):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:]) / scores[0]

    high_students = 0
    for score in scores[1:]:
        if score > avg:
            high_students += 1

    rates = high_students / scores[0] * 100
    print('%.3f'%rates+'%')