# 문제: https://www.acmicpc.net/problem/9012

t = int(input())

for _ in range(t):
    parenthesis = list(input())
    checker = []
    result = True
    for p in parenthesis:
        if p == "(":  # 괄호가 "(" 이면 리스트에 append
            checker.append(p)
        else:  # 괄호가 ")" 인 경우
            if len(checker) == 0:  # 처음 괄호로 ")" 가 오는 경우 반복문 종료
                result = False
                break
            checker.pop()  # 괄호가 ")" 인 경우 리스트의 요소를 pop

    if result == True:
        if len(checker) == 0:  # 리스트에 남아 있는 요소가 없을 시 "YES" 출력
            print("YES")
        else:  # 리스트에 요소가 남아 있으면 괄호가 짝이 맞지 않은 것.
            print("NO")
    else:
        print("NO")