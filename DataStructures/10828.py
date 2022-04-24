# 문제: https://www.acmicpc.net/problem/10828

import sys

class stack:
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
    def size(self):
        return len(self.items)
    def isEmpty(self):
        if len(self.items) == 0:
            return(1)
        else:
            return(0)

stk = stack()
n = int(input())
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        stk.push(command[1])
    elif command[0] == "pop":
        print(stk.pop())
    elif command[0] == "top":
        print(stk.top())
    elif command[0] == "size":
        print(stk.size())
    elif command[0] == "empty":
        print(stk.isEmpty())