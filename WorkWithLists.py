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
StartTime = time.time()
OriginalList = ['one', 'two', 'three', ]
AddList = ['two', ]
DeleteList = ['two', 'five']


def GetSortedList(a: list, b: list) -> list:
    """Do unique list and sort list"""
    return sorted(list(set(a) - set(b)), key=lambda item: (len(item), item), reverse=True)


OriginalList.extend(AddList)
print(GetSortedList(OriginalList, DeleteList))
print(f"Time Execute:{time.time() - StartTime:.2f} sec")
