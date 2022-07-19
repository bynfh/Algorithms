class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    flag_stop_iter = False

    def __init__(self, data):
        self.node = Node(data)

    def append(self, value):
        end = Node(value)
        n = self.node

        while n.next:
            n = n.next

        n.next = end

    def __repr__(self):
        result = []
        n = self.node
        result.append(n.data)

        while n.next:
            n = n.next
            result.append(n.data)

        return f"{result}"

    def __next__(self):
        if self.node.next:
            result = self.node.data
            self.node = self.node.next
            return result

        if self.flag_stop_iter:
            raise StopIteration

        result = self.node.data
        self.flag_stop_iter = True

        return result

    def __iter__(self):
        return self
