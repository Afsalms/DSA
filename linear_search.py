"""
Linear search is a simple search algorithm for find a element in array
linear search time is linear with size of the array
worst case for linear search is O(n)
traverse through the array till match is found
"""
import random

def linear_search(array, element):
    for index, item in enumerate(array):
        if item == element:
            return True, index
    return False, None



array = list(range(100))
random.shuffle(array)
number = int(input("Enter the element to find :\n"))
found, position = linear_search(array, number)

if found:
    print(f"{number} is found at the index {position}")
else:
    print(f"{number} is not in the array")


