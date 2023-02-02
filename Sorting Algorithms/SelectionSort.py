'''
Author : Karthik Goudar
Date   : 2 Feb 2023


Simple Selection Sort Algorithm

Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the
unsorted part of the list and swapping it with the first unsorted element.

The minimum element from the unsorted part of the list is selected and swapped with the first unsorted element.
 This process is repeated until the entire list is sorted in ascending order.
'''



def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
print("Sorted array is:", selectionSort(arr))

