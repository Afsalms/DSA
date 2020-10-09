import math


def interpolation_search(array, x, l, h):
    print(l, h)

    pos = l + ( ((x - array[l]) * (h - l)) /(array[h] - array[l]))
    pos = math.floor(pos)
    if pos < l or pos > h:
        print("Element not found")
        return -1
    if pos >= len(array) or pos < 0:
        print("Element not found")
        return -1
    if array[pos] ==  x:
        print(f"Element found at {pos}")
        return pos
    elif array[pos] < x:
        return interpolation_search(array, x, pos+1, h)
    else:
        return interpolation_search(array, x, l, pos - 1)



#a = list(range(11))
a = [1, 3, 9, 15, 25, 55, 60]

index = interpolation_search(a, 50, 0, 6)

print("Array: ", a)
print("Index: ", index)
