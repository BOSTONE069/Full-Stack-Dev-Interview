def merge_sort(arr):
    """
    The given Python function implements the merge sort algorithm to sort an input array in ascending
    order.
    """
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left_half_array = merge_sort(arr[:middle])
    right_half_array = merge_sort(arr[middle:])
    return merged_array(left_half_array, right_half_array)

def merged_array(left, right):
    """
    The function `merged_array` takes two sorted arrays as input and merges them into a single sorted
    array.
    """
    sorted_array = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1
    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])
    
    return sorted_array


array_values = [12, 4, 7, 2, 9, 5, 10]
sorted_array = merge_sort(array_values)
print("Sorted array:", sorted_array)
