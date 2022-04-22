# 문제: https://www.acmicpc.net/problem/8958

n = int(input())
quiz_result = [list(input()) for i in range(n)]

for a in quiz_result:
    score = 0
    total_score = 0

    for i in a:
        if (i == 'O'):
            score += 1
        else:
            score = 0
        total_score += score

    print(total_score)