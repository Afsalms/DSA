"""
Binary search is faster way to search element fron an array
binary search has O(log(n)) complexity 
one disadvantage of this algorithm is that the array must be
on sort order
"""
import time

def binary_search(array, element_to_find, start, end):
    mid = int((start + end)/2)
    if start > end:
        return False, None
    if array[mid] == element_to_find:
        return True, mid
    elif array[mid] > element_to_find:
        end = mid
    else:
        start = mid + 1
    return binary_search(array, element_to_find, start, end)

number = int(input("Enter the number of elements :\n"))
array = list(range(number))
element_to_find = int(input("Enter the element to find : \n"))

is_found, index = binary_search(array, element_to_find, 0, len(array)-1)
if is_found:
    print(f"{element_to_find} is on the index {index}")
else:
    print(f"{element_to_find} is not in the list")
