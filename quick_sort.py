"""
Quick sort is the one most favourite sorting algorithm used
but it has worst case of O(n^2) but average and best case for this
algoritm is n(log(n)).It is also using the divide and conquer implementation
First we decide a index point then move the ussualy last element then move all the
element smaller than this to right larger than to its left then repeat this by splitting 
to smaller arrays
"""
import random

def quick_sort(array):
    if not array:
        return []
    index_point = array[-1]
    lesser_array = []
    equal_array = []
    greater_array = []
    for i in array:
        if i > index_point:
            greater_array.append(i)
        elif i == index_point:
            equal_array.append(i)
        else:
            lesser_array.append(i)
    return quick_sort(lesser_array) + equal_array + quick_sort(greater_array)



number = int(input("Enter the number of elemetns: \n"))
array = list(range(number))
random.shuffle(array)

print(f'Input array is {array}')
sorted_array = quick_sort(array)
print(f'Sorted array is {sorted_array}')

