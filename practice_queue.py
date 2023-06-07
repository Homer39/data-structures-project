from practice_node import Node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):

        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return data

    def peek_head(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def peek_tail(self):
        if self.is_empty():
            return None
        else:
            return self.tail.data

    def __str__(self):
        current = self.head
        items = []
        while current:
            items.append(current.data)
            current = current.next

        return f"Stack({', '.join(items)})"


if __name__ == "__main__":
    queue = Queue()

    # enq
    queue.enqueue('1')
    queue.enqueue('2')

    print(queue)

    # deq
    queue.dequeue()
    print(queue)
