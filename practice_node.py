class Node:
    #data - данные
    #next - ссылка на объект предыдущий

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


if __name__ == "__main__":
    n1 = Node(5, None)
    n2 = Node(2, n1)

    print(n1.data)
    print(n2.data)
