# 문제: https://www.acmicpc.net/problem/1978
import sys

n = int(sys.stdin.readline())
numbers = sys.stdin.readline().split()

result = 0

for i in range(n):
    isPrime = False
    if int(numbers[i]) > 2:
        for j in range(2, int(numbers[i])): # 소수 판별 알고리즘
            if int(numbers[i]) % j == 0:
                isPrime = False
                break
            else:
                isPrime = True
    elif int(numbers[i]) == 2:
        isPrime = True

    if isPrime:
        result += 1

print(result)