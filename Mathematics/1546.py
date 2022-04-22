# 문제: https://www.acmicpc.net/problem/1546

n = int(input())
scores = list(map(int, input().split()))
max_scores = max(scores)
new_scores = [(i / max_scores * 100) for i in scores]
print(sum(new_scores) / len(new_scores))