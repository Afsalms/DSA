import random

def prepend_zero(array):
    max_value = max(array)
    length = len(str(max_value))
    formated_array = []
    for i in array:
        if len(str(i)) != length:
            zeros = (length - len(str(i))) * "0"
            formated_array.append(zeros + str(i))
        else:
            formated_array.append(str(i))
    return formated_array, length

def create_bucket():
    return {str(i): []  for i in range(10)}

def radix_sort(array):
    formated_array, iteration = prepend_zero(array)
    for i in range(iteration-1, -1, -1):
        bucket = create_bucket()
        for item in formated_array:
            digit = item[i]
            bucket[digit].append(item)
        formated_array = []
        for i in bucket:
            if bucket.get(i):
                formated_array.extend(bucket.get(i))
    return [int(i) for i in formated_array]



array = list(range(15))


random.shuffle(array)

sorted_array = radix_sort(array)

print("Input array:  ", array)
print("Sorted array: ",sorted_array)
