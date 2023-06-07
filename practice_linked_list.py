from practice_node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_to_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_to_index(self, index, data):

        new_node = Node(data)
        if index == 0:
            self.insert_to_start(data)
            # new_node.next = self.head
            # self.head = new_node
            return

        current = self.head
        previous_node = None
        current_index = 0

        while current_index < index and current is not None:
            previous_node = current
            current = current.next
            current_index += 1
        if current is None:
            previous_node.next = new_node
        else:
            new_node.next = current
            previous_node.next = new_node
