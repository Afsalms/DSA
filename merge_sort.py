"""
Merge sort is one of the efficient sorting algorithm
with logarithimic complexity its has best, worst, average
complexity of nlog(n). It uses divide and conquer approch
split the array till array become elementary then merge the 
array based on the order
"""
import random

def merge_array(left, right):
    """
    compare first elemet of each arrays then push that value to
    a list then remove the pushed value again compare till one of the
    array become empty after than push the entire element of array  of element
    which is not empty
    """
    merged_array = []
    while len(right) and len(left):
        if right[0] < left[0]:
            merged_array.append(right[0])
            del(right[0])
        else:
            merged_array.append(left[0])
            del(left[0])
    if left:
        merged_array += left
    if right:
        merged_array += right
    return merged_array 



def merge_sort(array):
    """
    This function split the array in to smaller array
    till the len of the array become one
    """
    if len(array) <= 1:
        return array
    mid = int((len(array)/2))
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge_array(left, right)


number = int(input("Enter the number of elements: \n"))

array = list(range(number))

random.shuffle(array)

print(f"Input array is {array}")

result = merge_sort(array)


print(f"Print sorted array is : {result}")


