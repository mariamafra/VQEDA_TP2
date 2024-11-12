
import random

def merge_sort(registros):
    if len(registros) <= 1:
        return registros
    
    mid = len(registros) // 2
    left_half = merge_sort(registros[:mid])
    right_half = merge_sort(registros[mid:])
    
    return merge(left_half, right_half)


def merge(left, right):
    sorted_list = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    sorted_list.extend(left[left_index:])
    
    sorted_list.extend(right[right_index:])
    
    return sorted_list

random_records = random.sample(range(1, 10**7), 5_000_000)
sorted_records = merge_sort(random_records)
len(sorted_records)