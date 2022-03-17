# 문제: https://www.acmicpc.net/problem/4673

for i in range(1, 10000):
    isConstructor = False
    for j in range(1, i):
        str_num = str(j)
        ciphers_sum = 0
        for h in range(0, len(str_num)): # 자릿수의 합 계산
            ciphers_sum += int(str_num[h])

        if j + ciphers_sum == i:
            isConstructor = True
            break
        else:
            isConstructor = False

    if isConstructor == False:
        print(i)