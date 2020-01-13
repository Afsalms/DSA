"""
Bubble sort algorithm is a simple sorting algorithm
in which largest element is moved to the right in each 
iteration worst case for this algorithm os O(n^2)
we use a flag is_sorted so that if there is no swapping
in any iteration which mean the array is sorted. In that case we
break the code.is_sorted flag increase the efficiency of the algorithm
incase the input is already in sorted order
"""
import random

def bubble_sort(array):
    number_of_iteration = 0
    for i in range(len(array)):
        is_sorted = True
        for j in range(1,len(array)):
            number_of_iteration += 1
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                is_sorted = False
            print(f'{array=}')
        if is_sorted:
            break
    print(f"{number_of_iteration=} ")



if __name__ == "__main__":
    number = int(input("Enter the number of elements :\n"))
    array = list(range(number))
    is_shuffle_required = input("Do you need to shuffle the array: \n")
    if is_shuffle_required == "yes":
        random.shuffle(array)
    print(f"Input is : {array}")
    bubble_sort(array)
    print(f"Sorted array: {array}")


