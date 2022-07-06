class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(str(element))

    def pop(self):
        if self.data:
            last_element = self.data.pop()
            return last_element

    def top(self):
        if self.data:
            return self.data[-1]

    def is_empty(self):
        if self.data:
            return False
        return True

    def __str__(self):
        result = ', '.join(str(x) for x in sorted(self.data, reverse=True))
        return f"[{result}]"


# test zero
# stack = Stack()
# stack.push("apple")
# stack.push("carrot")
# print(str(stack))
# print(stack.pop())
# print(stack.top()) # 'apple'
# stack.push("cucumber")
# print(str(stack))
# print(stack.is_empty())


# test = Stack()
# print(test.push(2))
# print(test.push(3))
# print(test.push(4))
# print(test.pop())
# print(test.top())
# print(test.is_empty())
# print(test.push('a'))
# print(test.push('b'))
# print(str(test))