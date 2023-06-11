## Stacks ✔

class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
        
    def size(self):
        return len(self.stack)
    
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None
        
    def __str__(self):
        return str(self.stack)
    


stack = Stack()

print(stack.push(30))
print(stack.push(33))
print(stack.push(35))
print(stack.push(20))
print(stack.pop())
print(stack.size())
print(stack.peek())
print(stack.__str__())
