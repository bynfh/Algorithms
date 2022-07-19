from data_structures.linked_list.common_linked_list import Node

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
