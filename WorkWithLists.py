"""Inputs
- Original list of strings
- List of strings to be added
- List of strings to be removed

Return
- List shall only contain unique values
- List shall be ordered as follows
--- Most character count to least character count
--- In the event of a tie, reverse alphabetical

For example:

Original List = ['one', 'two', 'three',]
Add List = ['one', 'two', 'five', 'six]
Delete List = ['two', 'five']
Result List = ['three', 'six', 'one']"""


import time
"""I done it in python way and tried to done with algorithms, but in python way win in all test"""
#######################################################################################################################
"""First solve it is Python way."""
print("First solve:")
OriginalList = ['one', 'two', 'three', 'five', 'six', 'eighth', 'four']
AddList = ['two', 'five', 'nine', 'ten']
DeleteList = ['two']
StartTimeFirst = time.time()


def GetSortedList(a: list, b: list) -> list:
    """Do unique list and sort list"""
    return sorted(list(set(a) - set(b)), key=lambda item: (len(item), item), reverse=True)


OriginalList.extend(AddList)
print(GetSortedList(OriginalList, DeleteList))
print(f"Time execute:{time.time() - StartTimeFirst:.2f} Sec")
#######################################################################################################################
#######################################################################################################################
"""Second solve with algorithms.
I was wondering if i should delete elements from OriginalList and AddList. But IDK, because without delete.
Idea: Sorted, then """
StartTimeFirst = time.time()
print("\nWith algorithms:")
OriginalList = ['one', 'two', 'three', 'five', 'six', 'eighth', 'four']
AddList = ['two', 'five', 'nine', 'ten']
DeleteList = ['two', 'one', 'five', 'three', 'nine']
# Sort lists
OriginalList.sort(key=lambda item: (len(item), item), reverse=True)
AddList.sort(key=lambda item: (len(item), item), reverse=True)
DeleteList.sort(key=lambda item: (len(item), item), reverse=True)


def LowerBound(A: list, key: str) -> int:
    """Return index from list. It is binary search."""
    left = -1
    right = len(A)
    while right > left + 1:
        middle = (left + right) // 2
        if len(A[middle]) <= len(key):
            if A[middle] == key:
                right = middle
            elif len(A[middle]) == len(key) and A[middle] > key:
                left = middle
            else:
                right = middle
        else:
            left = middle
    return right


for element in DeleteList:
    if LowerBound(OriginalList, element):
        while True:
            try:
                OriginalList.remove(element)
            except ValueError:
                break
    if LowerBound(AddList, element):
        while True:
            try:
                AddList.remove(element)
            except ValueError:
                break
for element in AddList:
    if LowerBound(OriginalList, element):
        OriginalList.append(element)

OriginalList = list(set(OriginalList))
OriginalList.sort(key=lambda item: (len(item), item), reverse=True)
print(OriginalList)
print(f"Time execute:{time.time() - StartTimeFirst:.2f} Sec")
#######################################################################################################################

