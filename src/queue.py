class Node:
    """Класс для узла стека"""

    def __init__(self, data=None, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.tail = None
        self.head = None

    def is_empty(self):
        """
        Метод для проверки на наличие данных
        """
        return self.head is None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.is_empty():
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        current = self.head
        items = []
        while current:
            items.append(current.data)
            current = current.next

        return f"Stack({', '.join(items)})"


queue = Queue()
queue.enqueue('data1')
print(queue)
