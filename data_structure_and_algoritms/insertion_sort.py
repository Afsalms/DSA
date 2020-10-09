"""
Insertion sort algorithm is also a simple sort like
bubble sort here we select an index point initially 
pointed to the first element of the list then compare with
entire element in the list after first iteration first element will
be the smallest element. Then increment the index value compare with 
entire element greater than the index and so on this algorithm also
has worst case of O(n^2)
"""
import random

def insertion_sort(array):
    number_of_iteration = 0
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            number_of_iteration += 1
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
        print(f'{array=}')
    print(f'{number_of_iteration=}')

if __name__ == "__main__":
    number = int(input("Enter the number of elements: \n"))
    array = list(range(number))
    random.shuffle(array)
    print(f"input is : {array}")
    insertion_sort(array)
    print(f"sorted array is: {array}")
