# 문제: https://www.acmicpc.net/problem/1110

N = int(input())
new_number = N
cycle = 0

while True:
    new_number = int(str(new_number % 10) + str(sum(map(int, str(new_number))) % 10))
    cycle += 1

    if cycle != 0 and new_number == N: # 원래 수로 돌아왔을 경우 반복문 종료
        print(cycle)
        break
