class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, value):
        end = Node(value)
        n = self
        while n.next:
            n = n.next
        n.next = end


First = 1
Second = 2
Third = 3
LinkedList = Node(First)
LinkedList.append(Second)
LinkedList.append(Third)


Testing = LinkedList
print("Start testing")
assert Testing.data == First
while Testing.next:
    Testing = Testing.next
    First += 1
    assert Testing.data == First
print("Test successful")

