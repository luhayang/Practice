import sys

class Stack:
    def __init__(self):
        self.lst = []
    
    def push(self, num):
        return self.lst.append(num)
    
    def pop(self):
        try: return self.lst.pop()
        except IndexError: return -1

    def size(self):
        return len(self.lst)
    
    def empty(self):
        if len(self.lst) == 0: return 1
        else: return 0
    
    def top(self):
        try: return self.lst[-1]
        except IndexError: return -1

n = int(sys.stdin.readline())

s = Stack()

for i in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == "push": s.push(command[1])
    elif command[0] == "pop": print(s.pop())
    elif command[0] == "size": print(s.size())
    elif command[0] == "empty": print(s.empty())
    else: print(s.top())
