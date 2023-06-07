class Node:
    """Класс для узла стека"""

    def __init__(self, data=None, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None
        self.size = 0

    def __str__(self):
        return self.top

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        node = Node(data)
        node.next = self.top
        self.top = node
        self.size += 1

    def is_empty(self):
        """
        Метод для проверки на наличие данных
        """
        return self.top is None

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.is_empty():
            return None

        else:
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return data
