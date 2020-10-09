import math


def bubble_down(index, array, heap_type):
    left = (2*index)
    if left > len(array):
        return
    right = None
    if len(array) > (2* index) + 1:
        right = (2*index)+1
    if right and left:
        if heap_type == "max":
            child_index = right if array[right] > array[left] else left
        else:
            child_index = right if array[right] < array[left] else left
    else:
        child_index = left
    if right:
        print("right element: ", array[right])
    else:
        print("right element", "No child")
    print("Left element: ", array[left])
    if array[child_index] > array[index] and heap_type == "max":
        array[child_index], array[index] = array[index], array[child_index]
    elif array[child_index] < array[index] and heap_type == "min":
        array[child_index], array[index] = array[index], array[child_index]
    bubble_down(child_index, array, heap_type)

def heapify(array, heap_type="max"):
    array.insert(0, "dummy")
    start_index = int(math.floor((len(array)-1)/2))
    for i in range(start_index, 0, -1):
        bubble_down(i, array, heap_type)





array = [2,7,26,25,19,17,1,90,3,36]


print("Input: ", array)

heapify(array, "min")

array.pop(0)

print("Output", array)

if array == [1, 3, 2, 7, 19, 17, 26, 90, 25, 36]:
    print("algorithm is working properly")
else:
    print("Algorithm is not working")


