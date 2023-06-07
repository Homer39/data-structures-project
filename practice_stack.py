from practice_node import Node


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.size += 1

    def is_empty(self):
        return self.top is None

    def pop(self):
        if self.is_empty():
            return None

        data = self.top.data
        self.top = self.top.next
        self.size -= 1

        return data

    def get_size(self):
        return self.size

    def peek(self):
        return self.top.data

    def __str__(self):
        current = self.top
        items = []
        while current:
            items.append(current.data)
            current = current.next

        return f"Stack({', '.join(items)})"

if __name__ == "__main__":
    stack = Stack()

    #push
    stack.push('data1')
    stack.push('data2')

    print(stack)

    #pop
    stack.pop()
    print(stack)

    #peek
    print(stack.peek())
    stack.push('data3')
    print(stack.peek())