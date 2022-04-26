# 문제: https://www.acmicpc.net/problem/1874

class stack: # 1~n 수에 대해 push, pop 연산을 수행할 stack
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items.pop()
    def top(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items[len(self.items)-1]

n = int(input())
sequence = list(map(int, (input() for _ in range(n))))
stk = stack()
result = []
i = 0

for s in sequence:
    if s == stk.top(): # 수열의 현재 수가 stack의 top과 같은 수일 경우
        stk.pop()
        result.append("-")
        continue

    while (i <= n): # 1~n 수에 대해 차례로 push, pop 연산 수행
        i += 1
        stk.push(i)
        result.append("+")
        if s == i:
            stk.pop()
            result.append("-")
            break

count_pop = 0
for r in result:
    if r == "-":
        count_pop += 1

if count_pop == n: # 연산을 만들 수 있는 경우
    for r in result:
        print(r)
else: # 연산을 만들 수 없는 경우
    print("NO")