# 문제: https://www.acmicpc.net/problem/3052

numbers = [(int(input()) % 42) for i in range(10)]
numbers = list(set(numbers)) # set 함수를 이용해 중복 제거
print(len(numbers))