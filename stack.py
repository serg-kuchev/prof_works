class Stack:
    def __init__(self):
        self.new_stack = []

    def isempty(self):
        return self.new_stack == []

    def push(self, item):
        self.new_stack.append(item)

    def pop(self):
        return self.new_stack.pop()

    def peek(self):
        return self.new_stack[len(self.new_stack) - 1]

    def size(self):
        return len(self.new_stack)


def check_brackets(brackets):
    open_ = '([{'
    close = '}])'
    all_ = ['()', '[]', '{}']
    stack = Stack()
    for b in brackets:
        if b in open_:
            stack.push(b)
        elif b in close:
            if stack.isempty():
                stack.push(b)
            elif stack.peek() + b in all_:
                stack.pop()
    if stack.isempty():
        print("Сбалансированно")
    else:
        print("Несбалансированно")


check_brackets('')
