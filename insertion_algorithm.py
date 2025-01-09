def insertion_sort_descending(arr):
    """
    Perform Insertion Sort in descending order.
    
    Parameters:
        arr (list): A list of integers to be sorted.
        
    Returns:
        list: A list sorted in monotonically decreasing order.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift elements of arr[0..i-1] that are smaller than key
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    sample_array = [8, 2, 4, 1, 3]
    print("Original array:", sample_array)
    sorted_array = insertion_sort_descending(sample_array)
    print("Sorted array (descending):", sorted_array)

