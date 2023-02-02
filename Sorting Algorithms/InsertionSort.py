'''
Author : Karthik Goudar
Date   : 1 Feb 2023


Simple Insertion Sort Algorithm

Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time.
It is much less efficient than more advanced algorithms such as quicksort, heapsort, or merge sort.

Each element from the unsorted part of the list is selected and inserted into its correct position in the sorted part of the list.
This process is repeated until the entire list is sorted in ascending order.
'''



def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
print("Sorted array is:", insertionSort(arr))
