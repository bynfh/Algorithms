import random

from algorithms.sorts.merge_sort import merge_sort

lists = []
# Create some lists in list
for i in range(11):
    lists.append([random.randint(1, 100) for numb in range(10)])

print("==" * 10, "Start testing".upper(), "==" * 10)

for unsorted_list in lists:
    sorted_list = merge_sort(unsorted_list)
    print(f"Unsorted list:{unsorted_list}\n  Sorted list:{sorted_list}\n")
    assert sorted_list == sorted(unsorted_list), "PRIVET"

print("==" * 10, "Tests finished".upper(), "==" * 10)
