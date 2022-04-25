# 문제: https://www.acmicpc.net/problem/10845

import sys

class queue:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if len(self.items) == 0:
            return -1
        else:
            pop_number = self.items[0]
            del self.items[0]
            return pop_number
    def size(self):
        return len(self.items)
    def isEmpty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0
    def front(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items[0]
    def back(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items[len(self.items)-1]

que = queue()
n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        que.push(command[1])
    elif command[0] == "pop":
        print(que.pop())
    elif command[0] == "size":
        print(que.size())
    elif command[0] == "empty":
        print(que.isEmpty())
    elif command[0] == "front":
        print(que.front())
    elif command[0] == "back":
        print(que.back())